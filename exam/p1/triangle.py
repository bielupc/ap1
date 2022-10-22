import turtle as tl
from yogi import read


def dibuixar_triangle(m: float) -> None:
    """Dibuixa un triangle de costat m"""
    for i in range(3):
        tl.forward(m)
        tl.left(120)


def triangle_sierpinski (m: float, n: int) -> None:
    """Dibuixa el triangle de Sierpiński amb n nivels i una mida m per costat"""
    
    # Case base
    if n == 1: 
        dibuixar_triangle(m)

    # Cas recurssiu
    else:
        dibuixar_triangle(m)
        triangle_sierpinski(m/2, n-1)

        # Ajustaments pel segon sub-triangle
        tl.up()
        tl.forward(m/2)
        tl.down()

        triangle_sierpinski(m/2, n-1)

        #Ajustaments per l'últim sub-triangle
        tl.up()
        tl.right(60)
        tl.backward(m/2)
        tl.left(60)
        tl.down()

        triangle_sierpinski(m/2, n-1)

        #Retorn a la posició inicial
        tl.up()
        tl.left(60)
        tl.backward(m/2)
        tl.right(60)


def main() -> None:
    m = read(float)
    n = read(int)

    # Paràmetres de la tortuga
    tl.hideturtle()
    tl.speed(0)

    triangle_sierpinski(m, n)

    tl.done()


if __name__ == "__main__":
    main()
