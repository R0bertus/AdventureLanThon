from browser import window
from browser.timer import set_interval
from _functools import partial as function
_ = window.parent.jQuery
date = window.Date.new
now = window.Date.now


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