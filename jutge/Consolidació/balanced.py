from yogi import scan

def llargada(n: int) -> int:
    if n == 0:
        return 0
    else:
        return 1 + llargada(n//10)

def is_balanced(n: int) -> bool:
    """
    Donat un nombre natural n, retorna si la suma dels nombres en les posicions parelles
    es igual a la suma dels nombres en les posicions imparelles.
    """
    sum_parell = 0
    
    if llargada(n) % 2 != 0:
        for i in range(llargada(n) - 2):
            if i == 0:
                retall_esquerra = 1 # En la primera iteració no dividim
            else:
                retall_esquerra = 10 ** (2*i) # Tenim el deu seguit de zeros parells
            
            retall_dreta = (10 ** (2*i + 1)) # Tenim el deu seguit de zeros imparells

            sum_parell += (n % retall_dreta) // retall_esquerra # Retallem el nombre n per seleccionar el nombre i sumar-lo al total

def main() -> None:
    n = scan(int)
    while n is not None:
        print(is_balanced(n))
        n = scan(int)

if __name__ == "__main__":
    main()
