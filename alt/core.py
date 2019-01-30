from browser.timer import set_interval
from browser import window
from _functools import partial as function
_ = window.parent.jQuery
date = window.Date.new
now = window.Date.now


class AdventureLanThon(object):
    SKILL_DRINK_HEALTH = "use_hp"
    SKILL_DRINK_MANA = "use_mp"
    HEALTH_POTION = "hpot0"
    MANA_POTION = "mpot0"
    POTIONS = "potions"
    MONSTER = "monster"
    CHARACTER = "character"
    monsters = window.G.monsters
    character = window.character

    def __init__(self):
        self.target = None

    def get_position(self, target=character):
        try:
            return {"x": target.real_x, "y": target.real_y, "map": target.map}

        except AttributeError:
            return {"x": target.real_x, "y": target.real_y}

    def set_message(self, message, color="yellow"):
        window.set_message(message, color)

    def game_log(self, message, color="yellow"):
        window.game_log(message, color)

    def smart_move(self, location, callback=None):
        if type(location) is str:
            window.smart_move({"to": location}, callback)
        else:
            window.smart_move(location, callback)

    def buy_potions(self, health=0, mana=0):
        health = int(health)
        mana = int(mana)
        position = self.get_position()

        def on_success(done):
            if 0 < health:
                window.buy(self.HEALTH_POTION, health)
                self.game_log("Bought %s health potions" % health, "red")

            if 0 < mana:
                window.buy(self.MANA_POTION, mana)
                self.game_log("Bought %s mana potions" % mana, "blue")

            self.smart_move(position)

        self.smart_move(self.POTIONS, on_success)

    def get_nearest_monster(self, max_att=25, min_xp=10, target="", no_target=True):
        return window.get_nearest_monster({max_att: max_att, min_xp: min_xp, target: target, no_target: no_target})

    def use_hp_or_mp(self):
        window.use_hp_or_mp()

    def use(self, skill):
        window.use(skill)

    def drink_health(self, treshold=0.5):
        if self.character.hp / self.character.max_hp < treshold:
            self.use(self.SKILL_DRINK_HEALTH)
            return True
        else:
            return False

    def drink_mana(self, treshold=0.5):
        if self.character.mp / self.character.max_mp < treshold:
            self.use(self.SKILL_DRINK_MANA)
            return True
        else:
            return False

    def get_target(self):
        self.target = window.get_target()
        return self.target

    def loot(self):
        window.loot()

    def attack(self, target):
        window.attack(target)

    def heal(self, target):
        window.heal(target)

    def in_attack_range(self, target):
        return window.in_attack_range(target)

    def farm_nearest_monster_warrior_simple(self, maximum_attack=25, minimum_experience=10, treshold_hp=0.5, treshold_mp=0.4):
        if self.get_target() is None:
            monster = self.get_nearest_monster(maximum_attack, minimum_experience)
            self.smart_move(self.get_position(monster))
            self.attack(monster)
        else:
            if self.drink_health(treshold_hp):
                return True
            elif self.drink_mana(treshold_mp):
                return True
            else:
                if not self.in_attack_range(self.get_target()):
                    self.smart_move(self.get_position(self.get_target()))
                self.attack(self.get_target())


alt = AdventureLanThon()
farm_nearest_monster_warrior_simple = alt.farm_nearest_monster_warrior_simple
get_position = alt.get_position
set_message = alt.set_message
game_log = alt.game_log
smart_move = alt.smart_move
buy_potions = alt.buy_potions
get_nearest_monster = alt.get_nearest_monster
use_hp_or_mp = alt.use_hp_or_mp
drink_health = alt.drink_health
drink_mana = alt.drink_mana
get_target = alt.get_target
in_attack_range = alt.in_attack_range
attack = alt.attack
loot = alt.loot
heal = alt.heal
use = alt.use


class GoldMeter(object):
    def __init__(self):
        self.bottom_right_corner = _("#bottomrightcorner")
        self.bottom_right_corner.find("#goldtimer").remove()

        self.xpt_container = _('<div id="goldtimer"></div>').css({
            "fontSize": '28px',
            "color": 'white',
            "textAlign": 'center',
            "display": 'table',
            "overflow": 'hidden',
            "marginBottom": '-5px',
            "width": "100%"
        })

        self.xptimer = _('<div id="goldtimercontent"></div>').css({
            "display": 'table-cell',
            "verticalAlign": 'middle'
        }).html("").appendTo(self.xpt_container)

        self.bottom_right_corner.children().first().after(self.xpt_container)

        self.init_goldmeter()

    def init_goldmeter(self):
        self.sum_gold = 0
        self.start_time = now()
        try:
            window.parent.prev_handlers_goldmeter
        except:
            window.parent.prev_handlers_goldmeter = []

        if window.parent.prev_handlers_goldmeter:
            for event, handler in window.parent.prev_handlers_goldmeter:
                window.parent.socket.removeListener(event, handler)

        window.parent.prev_handlers_goldmeter = []

    def update_gold_timer_list(self):
        gold = self.get_gold_per_second()
        gold_string = "<div>" + str(gold) + " Gold/Hr" + "</div>"

        _('#' + "goldtimercontent").html(gold_string).css({
            "background": 'black',
            "border": 'solid gray',
            "borderWidth": '5px 5px',
            "height": '34px',
            "lineHeight": '34px',
            "fontSize": '30px',
            "color": '#FFD700',
            "textAlign": 'center',
        })

    def update_goldmeter(self):
        self.update_gold_timer_list()

    def get_gold_per_second(self):
        elapsed = now() - self.start_time
        gold_per_second = int((3600.0 / (elapsed / 1000.0)) * self.sum_gold)
        return int(gold_per_second)

    def register_goldmeter_handler(self, event, handler):
        window.parent.prev_handlers_goldmeter.append([event, handler])
        window.parent.socket.on(event, handler)

    def gold_meter_game_response_handler(self, event):
        if "response" in dir(event):
            if event.response == "gold_received":
                self.sum_gold += event.gold

    def gold_meter_game_log_handler(self, event):
        if "message" in dir(event):
            if event["color"] == "gold":
                gold = int(event["message"].replace(" gold", ""))
                self.sum_gold += gold


def enable_goldmeter():
    try:
        gold_meter = GoldMeter()
        gold_meter.register_goldmeter_handler("game_log", gold_meter.gold_meter_game_log_handler)
        gold_meter.register_goldmeter_handler("game_response", gold_meter.gold_meter_game_response_handler)
        set_interval(function(gold_meter.update_goldmeter), 100)
    except:
        pass











