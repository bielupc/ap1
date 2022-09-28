
def missatge(qui:str, verb:str, cops:int, fem:bool) -> None:
    if fem:
        art = "Na"
    else:
        art = "En"

    if cops == 0:
        print(art, qui, "no ha", verb+".")
    elif cops == 1:
        print(art, qui, "ha", verb, cops, "cop"+".")
    else:
        print(art, qui, "ha", verb, cops, "cops"+".")




