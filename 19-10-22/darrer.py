from yogi import tokens

def llegir_dades() -> list[int]:
    return list(tokens(int))


def comptar_ocurrencies(llista: list[int], element: int) -> int:
    c = 0
    for x in llista:
        if x == llista[-1]:
            c += 1
    return c 
    

def main() -> None:
    l = llegir_dades()
    # print(l.count(l[-1]))
    print(comptar_ocurrencies(l, l[-1]))
       

if __name__ == "__main__":
    main()
