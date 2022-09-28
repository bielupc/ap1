from yogi import read
import turtle as tl




def dibuixa_rellotge(r:int, l:int) -> None:
    """Dibuixa un rellotge amb el radi i la mida de les ratlles adequada"""

    tl.penup()
    tl.goto(0, -r)
    tl.pendown()
    tl.circle(r)
    tl.left(90)

    for i in range(12):

        tl.goto(r/3, r/4)
        #tl.goto(0, -r)
        tl.forward(l)
        tl.penup()
        tl.backward(l)

        tl.left(30)
        tl.pendown()

    




def main() -> None:
    h = read(int)
    m = read(int)
    
    tl.hideturtle()
    # tl.speed(0)

    dibuixa_rellotge(200, 50)
    tl.done()

if __name__ == "__main__":
    main()
