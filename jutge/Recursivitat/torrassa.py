from yogi import read

def campanades_minuts(m: int) -> int:
    if m == 0:
        return 4
    else:
        if m >= 15:
            if m >= 30:
                if m >= 45:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0


def contador(h: int, m: int, t: int) -> int:
    if t == 0:
        return 0
    else:
        if h == 0:
            contador_campanades = 12 + campanades_minuts(m)
        elif h == 12:
            contador_campanades = 100 + campanades_minuts(m)
        else:
            if t < 60:
                contador_campanades = h % 12 + campanades_minuts(m)
            else:




    return contador_campanades


def main() -> None:
    h = read(int)
    m = read(int)
    t = read(int)
    print(contador(h, m, t))


if __name__ == "__main__":
    main()
