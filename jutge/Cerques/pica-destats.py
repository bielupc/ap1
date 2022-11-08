from yogi import scan


def es_pic(x: int, y: int, z: int) -> bool:
    return y > x and y > z

def main() -> None:

    x = scan(int)
    y = scan(int)
    z = scan(int)

    mes_que_pica = False

    while z != 0 and not mes_que_pica and None not in (x, y, z):
        if es_pic(x, y, z) and y > 3143:
            mes_que_pica = True
        else:
            x, y, z = y, z, scan(int) 
    
    if mes_que_pica:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
