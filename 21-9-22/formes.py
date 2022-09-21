from turtle import *

# accions

def quadrat(mida: float) -> None:
    nagon(mida, 4)

def nagon(mida: float, costats:int) -> None:
    angle = 360/costats
    for i in range(costats):
        forward(mida)
        right(angle)

def quadrats_rotats(mida:float, nombre:int) -> None:
    angle = 360 / nombre
    for i in range(nombre):
        quadrat(mida)
        right(angle)

hideturtle()
speed(0)
quadrats_rotats(100, 120)
