from yogi import read, tokens, scan


def scalar_product(u: list[float], v: list[float]) -> float:
    s = 0.

    for i in range(len(u)):
        s += u[i] * v[i]
    return s

def main() -> None:
    u = [1.2, 3.4, 4.1]
    v = [5.1, 2.7, 1.3]

    print(scalar_product(u, v))

if __name__ == "__main__":
    main()
