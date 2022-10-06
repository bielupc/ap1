from turtle import *
from yogi import read


def koch(n: int, d: float) -> None:

    if n == -1:
        forward(d)
    else:

        koch(n - 1, d/3)
        left(60)
        koch(n - 1, d/3)
        right(120)
        koch(n - 1, d/3)
        left(60)
        koch(n - 1, d/3)

def floc_koch(n: int, d: float) -> None:
    
    for _ in range(3):
        koch(n, d)
        right(120)


def main() -> None:
    koch(2, 100)
    done()

if __name__ == "__main__":
    main()
