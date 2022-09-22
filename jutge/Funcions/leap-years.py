
def is_leap_year(y:int) -> bool:
    """Retorna si y és o no un leap year"""
    return ((y % 4) == 0 and str(y)[-2:] != "00") or (str(y)[-2:] == "00" and int(str(y)[:-2]) % 4 == 0)





