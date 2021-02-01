from layout_tools import *
from nice_arrays import *
import keyboard
from . import Ogham


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
            event.name,
            feather=False,
            return_lead=True,
            lead=ogham_lead,
        )
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
