def sumar1seg(h:int, m:int, s:int) -> tuple[int, int, int]:
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    return h, m, s

def sumar1seg2(hora:tuple[int, int, int]) -> tuple[int, int, int]:
    h, m, s = hora
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    return h, m, s




def main() -> None:
    h, m, s = 23, 59, 59
    h, m, s = sumar1seg2(h, m, s)
    print(h, m, s)

# les tuples son immutables
main()

