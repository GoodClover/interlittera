
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

BASIC_INPUT = [
    "backspace",
    "enter",
    "space",
    "delete",
    "left",
    "right",
    "up",
    "down",
    "end",
    "home"
]
C0_CONTROLLS = [chr(x) for x in range(0x00, 0x20)]
BASIC_LATIN = [chr(x) for x in range(0x20, 0x80)]
C0_CONTROLLS_AND_BASIC_LATIN = C0_CONTROLLS + BASIC_LATIN
