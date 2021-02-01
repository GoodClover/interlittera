# Imports


import keyboard
from nice_arrays import *


# Decorate your Christmas trees!


def escape(layout):
    def decor(event):
        if event.name == "esc":
            keyboard.unhook(decor)
            print("Disabled layout.")
            return
        layout(event)

    return decor


def basic_input(layout):
    def decor(event):
        if not layout(event):
            if event.name in BASIC_INPUT:
                keyboard.send(event.name)
                return

    return decor


def fallthrough(layout):
    def decor(event):
        if not layout(event):
            keyboard.send(event.name)
            return

    return decor


shift_store = False


def capitals(layout):
    def decor(event):
        global shift_store

        if event.name == "shift":
            shift_store = event.event_type == "down"
            return

        elif shift_store:
            if event.name in BASIC_LATIN:
                shift_store = False
                event.name = event.name.upper()
                return layout(event)

            else:
                shift_store = False
                keyboard.send("shift")
                return layout(event)

        return layout(event)

    return decor


def only_keyup(layout):
    def decor(event):
        if event.event_type == "up":
            layout(event)

    return decor


def only_keydown(layout):
    def decor(event):
        if event.event_type == "down":
            layout(event)

    return decor
