from yogi import read, scan, tokens

# formar paraules amb les lletres
# es poden repetir
# lletra del mig obligatoria
# minim de 3 lletres
# 3 lletres un punt, 4 lletres 2 punts, 5+ len(paraula) punts
# Tuti -> totes les lletres -> 10 punts extres

def tutti(w: str, lletres: str) -> bool:
    for l in lletres:
        if not l in w:
            return False
    return True



def punts(L: list, lletres: str) -> None:
    count = 0
    for w in L:
        l = len(w)
        if l >= 5:
            count += l
        elif l == 3:
            count += 1
        else:
            count += 2
        
        if tutti(w, lletres):
            count += 10
        
        
    print(count)

def ordenar(L: list) -> None:
    L.sort()
    for w in L:
        print(w)


def valida(paraula: str, lletres: str):
    """
    Retorna si la paraula compleix les normes del joc.
    """
    if len(paraula) < 3:
        return False
    
    if lletres[0] not in paraula:
        return False

    for l in paraula:
        if l not in lletres:
            return False
    return True


def main() -> None:
    lletres = read(str)
    paraula = scan(str)
    val: list[str] = list()

    while paraula is not None:
        if valida(paraula, lletres):
            val.append(paraula)
        
        paraula = scan(str)
    
    ordenar(val)
    print("-----")
    punts(val, lletres)


if __name__ == "__main__":
    main()
