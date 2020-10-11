from layout_tools import *
from nice_arrays import *
import keyboard


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
        keyboard.write(c)
