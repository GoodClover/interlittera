# Module imports
import keyboard
import importlib
from time import sleep

# Local imports
import layouts
from nice_arrays import *

hotkey = "altgr + semicolon"
release_key = "altgr"
in_change_mode = False
curr_layout = None


def enter_change_mode(from_hotkey=False):
    global in_change_mode

    if from_hotkey:
        keyboard.release(release_key)

    if curr_layout:
        keyboard.unhook(curr_layout)

    if in_change_mode:
        in_change_mode = False
        keyboard.unhook(change_mode)
        # s
        # keyboard.release("altgr")
        # keyboard.release("alt")
        # keyboard.release("shift")
        # keyboard.release("ctrl")
        print("Exited change mode.")
        return

    else:
        in_change_mode = True
        keyboard.hook(change_mode, suppress=True)
        change_to = ""
        print("Entered change mode.")
        return


change_to = ""


def change_mode(event):
    global change_to

    if event.name == "esc":
        enter_change_mode()

    elif event.name == "enter":
        print()
        enter_change_mode()
        change_to = change_to.strip()

        if change_to in layouts.layouts:
            curr_layout = layouts.layouts[change_to]
            keyboard.hook(curr_layout, suppress=True)

        elif change_to == "":
            print("Normal keyboard.")

        elif change_to == "reload":
            importlib.reload(layouts)

        elif change_to == "exit" or change_to == "quit":
            exit()

        else:
            print("Not a layout!")

        change_to = ""

    elif event.event_type == "up":
        if event.name == "backspace":
            change_to = change_to[:-1]
            print(f"\u001B[G{change_to} ", end="", flush=True)
        elif event.name in ALPHABET:
            change_to += event.name

    print(f"\u001B[G{change_to}", end="", flush=True)
    pass


def main():
    keyboard.add_hotkey(hotkey, enter_change_mode, args=(True,), suppress=True,
                        timeout=1, trigger_on_release=True)

    while True:
        sleep(60*60)
        print("T'as been hour, wot doing lad.")


if __name__ == "__main__":
    print("Please run __main__.py to start Interlittera, or run this whole directory to do it automatically.")
