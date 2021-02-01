from layout_tools import *
from nice_arrays import *
import keyboard


enm_lead = ""


matches_2 = {
    "Th": "Þ",
    "th": "þ",
    "Dh": "Ð",
    "dh": "ð",
    "Gh": "Ȝ",
    "gh": "ȝ",
}

matches_1 = {
    #     "Y": "Ȝ",
    #     "y": "ȝ",
    #     "W": "Ƿ",
    #     "w": "ƿ",
}
# TODO: Long s


@escape
@capitals
@only_keyup
@fallthrough
def layout_enm(event):
    global enm_lead

    print(event.name)

    if event.name.lower() in BASIC_LATIN:
        enm_lead += event.name

        if len(enm_lead) and enm_lead[-1] in matches_1:
            keyboard.write(matches_1[enm_lead[-1]])
            enm_lead = ""
            return True

        elif len(enm_lead) > 1 and enm_lead[-2:] in matches_2:
            keyboard.send("backspace")
            keyboard.write(matches_2[enm_lead[-2:]])
            enm_lead = ""
            return True

        else:
            return False

    else:
        print(event.name)
        enm_lead = ""
        return False