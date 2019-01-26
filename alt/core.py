import random

try:
    from browser import window
except ImportError:
    from alt.window import Window as window


def random_color():
    return "#" + hex(random.randint(0, 16777216)).split("x")[-1]


def set_message(message, color="yellow"):
    window.set_message(message, color)
