from yogi import scan

def sumar(a: int, b: int, k: int, i: int, sum: float) -> float:
    denom = a + i*k

    if denom > b:
        return sum
    else:
        i += 1
        sum += 1/denom
        return sumar(a, b,k, i, sum)




def main() -> None:
    a = scan(int)
    b = scan(int)
    k = scan(int)
    
    while a is not None and b is not None and k is not None:
        i = 0
        sum = 0
        print(f"{sumar(a, b, k, i, sum):.4f}")
        
        a = scan(int)
        b = scan(int)
        k = scan(int)

if __name__ == "__main__":
    main()
