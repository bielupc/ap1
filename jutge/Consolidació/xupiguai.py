from yogi import read


def cambiar_base(n: int, b: int) -> str:
    res = ""
    while n != 0:
        r = n % b
        res = str(r) + res
        n = n // b
    return res

def llargada(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + llargada(n//10)

def es_xupiguai(n: int, b: int) -> bool:
    n = cambiar_base(n, b)
    b2 = b//2
    l = llargada(int(n))
    if l % 2 == 0:

        
        
        






def main() -> None:
    n = read(int)
    b = read(int)

    print(es_xupiguai(n, b))

if __name__ == "__main__":
    main()
