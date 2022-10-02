

def is_leap_year(y:int) -> bool:
    """Retorna si y és o no un leap year"""
    return ((y % 4) == 0 and str(y)[-2:] != "00") or (str(y)[-2:] == "00" and int(str(y)[:-2]) % 4 == 0)


def ajustar_mes(d: int, m: str, a: int) -> tuple[int, str, int]:
    """donat un mes el passa al seguent i si es final d'any suma un any"""
    if m == "gener":
        return d, "febrer", a
    elif m == "febrer":
        return d, "marc", a
    elif m == "marc":
        return d, "abril", a
    elif m == "abril":
        return d, "maig", a
    elif m == "maig":
        return d, "juny", a
    elif m == "juny":
        return d, "juliol", a
    elif m == "juliol":
        return d, "agost", a
    elif m == "agost":
        return d, "setembre", a
    elif m == "setembre":
        return d, "octubre", a
    elif m == "octubre":
        return d, "novembre", a
    elif m == "novembre":
        return d, "desembre", a
    else:
        return d, "gener", a+1


def ajustar_dia(d: int, m: str, a: int, leap: bool) -> tuple[int, str, int]:
    """sumat un dia, comprova si correspon a un nou mes"""
    if d == 31 and (m == "gener" or m == "marc" or m == "maig" or m == "juliol" or m == "agost" or m == "octubre" or m == "desembre"):
        d = 1
        return ajustar_mes(d, m, a)
    elif d == 30 and (m == "abril" or m == "juny" or m == "setembre" or m == "novembre"):
        d = 1
        return ajustar_mes(d, m, a)
    elif d == 28 and m == "febrer" and not leap:
        d = 1
        return ajustar_mes(d, m, a)
    elif d == 29 and m == "febrer" and leap:
        d = 1
        return ajustar_mes(d, m, a) 
    else:
        return d+1, m, a
    


def dia_seguent(d: int, m: str, a: int) -> tuple[int, str, int]:
    """Retorna la data del dia seguent donada una data"""
    # d += 1
    leap = is_leap_year(a)
    return ajustar_dia(d, m, a, leap)



