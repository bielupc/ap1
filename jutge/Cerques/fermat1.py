from yogi import read
from math import sqrt, floor

def quadrat_perfecte(n: int) -> bool:
    arrel = sqrt(n)
    return arrel == floor(arrel)

def calcular_fermat(x: int, y: int) -> tuple[int, int, int, int]:
    z_quadrat = x ** 2 + y ** 2
    z = floor(sqrt(z_quadrat))
    return x, y, z, z_quadrat



def comprovar_fermat(x: int, y: int) -> str:
    x, y, z, z_quadrat = calcular_fermat(x, y)

    if quadrat_perfecte(z_quadrat):
        return f"{x}^2 + {y}^2 = {z}^2"
    else:
        return "No solution!"

def imprimir(a: int, b: int, c: int, d: int) -> str:

    for i in range(a, b+1):
        for j in range(c, d+1):
            text = comprovar_fermat(i, j)
            if text != "No solution!":
                return text
    return "No solution!"
 


def main() -> None:

    a = read(int)
    b = read(int)
    c = read(int)
    d = read(int)
   
    print(imprimir(a, b, c, d))



if __name__ == "__main__":
    main()









