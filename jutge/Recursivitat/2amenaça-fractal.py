import turtle as tl
from yogi import read


def amenaça_fractal(n: int, d: float) -> None:
    if n == 1:
        for i in range(4):
            tl.fd(d)
            tl.left(90)
    else:
        for i in range(4):
            tl.fd(d)
            tl.left(90)
        tl.up()
        tl.fd(d)
        tl.left(90)
        tl.fd(d)
        tl.right(90)
        tl.down()

        amenaça_fractal(n - 1, d/2)

        tl.up()
        tl.backward(d + d/2)
        tl.down()

        amenaça_fractal(n - 1, d/2)

        tl.up()
        tl.right(90)
        tl.fd(d + d/2)
        tl.left(90)
        tl.down()

        amenaça_fractal(n - 1, d/2)

        tl.up()
        tl.fd(d/2)
        tl.left(90)
        tl.fd(d/2)
        tl.right(90)
        tl.down()


def main() -> None:
    n = read(int)
    d = read(float)

    tl.speed(0)
    tl.hideturtle()
    tl.up()
    tl.goto(-d/2, -d/2)
    tl.down()

    amenaça_fractal(n, d)

    tl.done()

if __name__ == "__main__":
    main()
