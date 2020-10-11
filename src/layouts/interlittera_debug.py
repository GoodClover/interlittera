from layouts.layout_tools import *
import keyboard


@escape
def layout_debug(event):
    print(event)


@escape
@only_keyup
def layout_passthrough(event):
    keyboard.send(event.name)
