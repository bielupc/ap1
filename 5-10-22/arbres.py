from turtle import *



def arbre(n: int, d: float, a: float) -> None:
    if n == 0:
        forward(d)
        backward(d)
        

    else:
        forward(d)
        left(a / 2)
        arbre(n - 1, d*3/4, a)
        right(a)
        arbre(n-1, d*3/4, a)
        left(a / 2)
        backward(d)




def main() -> None:
    left(90)
    hideturtle()
    speed(0)
    arbre(5, 200, 30)
    done()

if __name__ == "__main__":
    main()
