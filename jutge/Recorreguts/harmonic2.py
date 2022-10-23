from yogi import scan 

def harmonic(n: int, m: int) -> float:
    har = 0.0
    for i in range(m+1, n+1):
        har += 1/i
    return har

def main() -> None:

    n = scan(int)
    m = scan(int)
    
    while n is not None and m is not None:

        print("{:.10f}".format(harmonic(n, m)))
        n = scan(int)
        m = scan(int)

if __name__ == "__main__":
    main()






