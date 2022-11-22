from statistics import harmonic_mean
from yogi import read

def solve_hanoi(n: int, a: int, b: int, c: int) -> None:
    if n > 0:
        solve_hanoi(n - 1, c, b)



def main() -> None:
    n = read(int)
    solve_hanoi(a, a, 0, 0)


if __name__ == "__main__":
    main()
