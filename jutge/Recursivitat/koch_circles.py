import turtle as tl
from yogi import read

def ajustar(d: float) -> None:
    tl.up()
    tl.right(90)
    tl.forward(d)
    tl.left(90)
    tl.forward(d)
    tl.right(90)
    tl.down()


def dibuixar_cercle(n: int, d: float) -> None:
    if n == 1:
        tl.circle(d)
    else:
        tl.circle(d)
        tl.up()
        tl.left(90)
        tl.forward(d)
        tl.right(90)
        tl.forward(d)
        tl.right(90)
        tl.down()
        dibuixar_cercle(n - 1, d/2)
        ajustar(d)
        dibuixar_cercle(n - 1, d/2)
        ajustar(d)
        dibuixar_cercle(n - 1, d/2)
        ajustar(d)
        dibuixar_cercle(n - 1, d/2)

        tl.up()
        tl.right(90)
        tl.forward(2 * d)
        tl.left(90)



def main() -> None:
    # n = read(int)
    # d = read(float)
    n = 6
    d = 100

    # tl.hideturtle()
    tl.speed(0)
    tl.up()
    tl.goto(0, -d)
    tl.down()
    dibuixar_cercle(n, d)

    tl.done()

if __name__ == "__main__":
    main()
