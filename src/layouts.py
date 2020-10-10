
# Module imports
import keyboard
import unicodedata

# Local imports
from nice_arrays import *
import Ogham


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

# Layout functions


@escape
def layout_debug(event):
    print(event)


@escape
@only_keyup
def layout_passthrough(event):
    keyboard.send(event.name)


@escape
@only_keyup
@basic_input
def layout_tags(event):
    c = None
    if event.name in BASIC_LATIN:
        c = chr(ord(event.name) + 0xE0000)
    elif event.name == "space":
        c = chr(0xE0020)
    elif event.name == "delete":  # delete becomes TAG CANCEL (corresponds)
        c = chr(0xE007F)
    elif event.name == "insert":  # insert becomes LANGUAGE TAG (deprecated)
        c = chr(0xE0001)
    if c:
        print(unicodedata.name(c))
        keyboard.write(c)


ogham_lead = ""


@escape
@only_keyup
@basic_input
def layout_ogham(event):
    global ogham_lead
    if event.name.lower() in BASIC_LATIN:
        if ogham_lead != "":
            keyboard.send("backspace")
        text, ogham_lead = Ogham.ogham(
            event.name, feather=False, return_lead=True, lead=ogham_lead)
        keyboard.write(text)
        if ogham_lead != "":
            keyboard.write(Ogham.ogham(ogham_lead, feather=False))
        return True
    elif event.name == "space":
        ogham_lead = ""
        keyboard.write(Ogham.ogham(" ", feather=False))
        return True
    elif event.name == "enter":
        keyboard.write(Ogham.characters["feather"]["tail"])
        keyboard.send("enter")
        keyboard.write(Ogham.characters["feather"]["head"])
        ogham_lead = ""
        return True
    elif event.name == "home":
        keyboard.write(Ogham.characters["feather"]["head"])
        return True
    elif event.name == "end":
        keyboard.write(Ogham.characters["feather"]["tail"])
        return True
    elif event.name in BASIC_INPUT:
        # Stop the combining thing, as the cursor most likely will have moved.
        ogham_lead = ""
        return False  # We still want @basic_input to handle the event.


# Layout list
layouts = {
    "debug": layout_debug,
    "passthrough": layout_passthrough,
    "tags": layout_tags,
    "ogham": layout_ogham
}
