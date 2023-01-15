import turtle
import easyinput

# constant amb la mida de l'àrea on cal dibuixar
MIDA = 300


def move_to(x, y):
    """Com el turtle.goto() però sense pintar."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def dibuixa_barra(i, amplada, valor):
    """
    Dibuixa una barra d'histograma amb una alçada valor a la columna i
    sabent que les barres tenen amplada amplada.
    """
    move_to(i * amplada, 0)
    for i in [1, 2]:
        turtle.forward(amplada)
        turtle.left(90)
        turtle.forward(valor)
        turtle.left(90)


def escriu_numero(x, y, numero):
    """
    Dibuixa el número numero a la posició x i y amb un sol decimal.
    """
    move_to(x, y)
    turtle.write(str(round(numero, 1)))


def main():
    """
    Dibuixa l'histograma del problema.
    """

    # accelerar dibuix
    turtle.hideturtle()
    turtle.speed(0)

    # llegir entrada
    barres = easyinput.read(int)
    dades = list(easyinput.read_many(int))

    # calcular amplada de les barres i comptar quants elements té cadascuna
    amplada = max(dades) / (barres-1)
    comptadors = [0 for i in range(barres)]
    for dada in dades:
        on = int(dada / amplada)
        if on == barres:
            on -= 1
        comptadors[on] += 1

    # dibuixar les barres
    alcada = max(comptadors)
    for i in range(barres):
        dibuixa_barra(i, MIDA / barres, comptadors[i] * MIDA / alcada)

    # dibuixar els números
    for i in range(barres + 1):
        escriu_numero(MIDA / barres * i, -10, amplada*i)


main()
