from yogi import read


# parametres formals
def maxim2(a: int, b: int) -> int: #capçelera
    """Retorna el màxim de dos valors enters.""" #especificació, que fa sense com ho fa
    if a > b:
        return a
    else:
        return b

def maxim3(a: int, b: int, c: int) -> int:
    """Retorna el màxim de tres valors enters"""
    return maxim2(maxim2(a, b), c)

# precondició
def factorial(n: int) -> int:
    """Donar un valor n positiu o zero, calcula el factorial de n"""
    f = 1
    for i in range(2, n+1):
        f = f*i
    return f

def binomial(n: int, k: int) -> int:
    """sfsdfsdf"""
    #variables locals

    return factorial(n) // (factorial(k) * factorial(n-k))

def mitjana(a: float, b: float) -> float:
    return (a+b) / 2



def main() -> None:
    a = read(int)
    b = read(int)
    c = read(int)
    #invocar la funció
    print(maxim3(a, b, c))
    #parametres reals
    n = read(int)
    k = read(int)

    c = factorial(n) // (factorial(k) * (factorial(n-k)))
main()

