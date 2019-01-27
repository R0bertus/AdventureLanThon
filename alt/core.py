from browser import window

class AdventureLanThon(object):
    LOCK = False
    POTIONS = "potions"
    HEALTH_POTION = "hpot0"
    MANA_POTION = "mpot0"
    character = window.character

    def __init__():
        pass

    def get_position(self):
        print(self.character)
        return {"x": self.character.real_x, "y": self.character.real_y, "map": self.character.map}

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

            print(position)
            self.smart_move(position)

        self.smart_move(self.POTIONS, on_success)
