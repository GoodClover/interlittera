
replacements = {
    "j": "g",
    "k": "q",
    "v": "f",
    "w": "uu",
    "x": "z",
    "y": "i"
}

characters = {
    "individual": {
        " ": "\u1680",
        "b": "\u1681",
        "l": "\u1682",
        "f": "\u1683",
        "s": "\u1684",
        "n": "\u1685",
        "h": "\u1686",
        "d": "\u1687",
        "t": "\u1688",
        "c": "\u1689",
        "q": "\u168a",
        "m": "\u168b",
        "g": "\u168c",
        "z": "\u168e",
        "r": "\u168f",
        "a": "\u1690",
        "o": "\u1691",
        "u": "\u1692",
        "e": "\u1693",
        "i": "\u1694",
        "p": "\u169a"
    },
    "combination": {
        "ae": "\u1699",
        "ea": "\u1695",
        "ia": "\u1698",
        "oi": "\u1696",
        "ui": "\u1697"
    },
    "feather": {
        "head": "\u169b",
        "tail": "\u169c"
    }
}

leadons = ["a", "e", "i", "o", "u"]

REPLACEMENT = "\uFFFD"


# for bip in characters:
#     for boop in characters[bip]:
#         print(f"{boop}: {characters[bip][boop]}")


def ogham(s, feather=True, replace_invalid="no", return_lead=False, lead=""):
    s = s.lower()

    # Replacements
    # This created a bug where "uwi" -> "uuui" which gets seen as "uu(ui)".
    # This created a bug where "ya" -> "ia" which gets seen as "(ia)".
    # This created a bug where "oy" -> "oi" which gets seen as "(oi)".
    # This created a bug where "uy" -> "ui" which gets seen as "(ui)".
    new = ""
    for c in s:
        if c in replacements:
            new += replacements[c]
        else:
            new += c
    s = new

    # Transliteration
    new = ""
    for c in s:
        if lead == "" and c in leadons:
            lead = c
        elif lead+c in characters["combination"]:
            new += characters["combination"][lead+c]
            lead = ""
        else:
            if lead in characters["individual"]:
                new += characters["individual"][lead]
            else:
                new += lead
            lead = ""

            if c in leadons:
                lead = c
            elif c in characters["individual"]:
                new += characters["individual"][c]
            else:
                if replace_invalid == "no":
                    new += c
                elif replace_invalid == "remove":
                    pass
                elif replace_invalid == "replacement":
                    new += REPLACEMENT
                else:
                    new += replace_invalid

    if (not return_lead) and lead != "":
        if lead in characters["individual"]:
            new += characters["individual"][lead]
        else:
            new += lead
        lead = ""

    if feather:
        new = \
            characters["feather"]["head"] + \
            new + \
            characters["feather"]["tail"]

    if return_lead:
        return new, lead
    else:
        return new


if __name__ == "__main__":
    print(ogham("Hello, my name is Oliver!"))
    print(ogham("Hello, my name is Oliver!", replace_invalid="no"))
    print(ogham("Hello, my name is Oliver!", replace_invalid="remove"))
    print(ogham("Hello, my name is Oliver!", replace_invalid="replacement"))
    print(ogham("ya"))
    print(ogham("uwi"))
