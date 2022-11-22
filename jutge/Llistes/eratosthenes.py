from yogi import scan
def eratosthenes(n: int) -> list[bool]:
    primes = [True for x in range(n+1)]
    primes[0] = False
    primes[1] = False

    i = 2
    while i*i <= n:
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
        i += 1
    return primes

def main():
    primes = eratosthenes(10**6)
    n = scan(int)
    while n is not None:
        if primes[n]:
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime")
        n = scan(int)
if __name__ == "__main__":
    main()
