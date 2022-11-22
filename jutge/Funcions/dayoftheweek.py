from math import floor


def day_of_the_week(d : int, m : int, y : int) -> str:
    """Donat un dia d, mes m i any y retorna un dia de la setmana corresponent"""
    m -= 2

    if m <= 0:
        m += 12
        y -= 1

    c = y // 100
    a = y % 100

       
    f = (floor((2.6 * m) - 0.2) + d + a + floor(a / 4) + floor(c / 4) - 2 * c) % 7

    if f == 0:
        return "Sunday" 
    elif f == 1:
        return "Monday" 
    elif f == 2:
        return "Tuesday"
    elif f == 3:
        return "Wednesday"
    elif f == 4:
        return "Thursday"
    elif f == 5:
        return "Friday"
    else:
        return "Saturday"

