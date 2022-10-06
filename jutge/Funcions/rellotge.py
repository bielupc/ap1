from yogi import read
import turtle as tl

def dibuixa_rellotge(r:int, l:int) -> None:
    """Dibuixa un rellotge amb el radi i la mida de les ratlles adequada"""

    tl.penup()
    tl.goto(0, -r)
    tl.pendown()

    for i in range(1, 12+1):
        tl.circle(r, 30)
        tl.left(90)
        tl.forward(l)
        tl.penup()
        tl.backward(l)
        tl.pendown()
        tl.right(90)
    tl.left(90)

def dibuixar_triangle(c:int) -> None:
    tl.right(30)
    tl.backward(c)
    tl.right(60)
    tl.forward(c)
    tl.left(120)
    tl.forward(c)
    tl.right(60)
    tl.setheading(90)

def dibuixar_busca(t:int, l:int, c:int) -> None:
    tl.penup()
    tl.goto(0, 0)
    tl.pendown()
    if t == 0:
        t = 12
    tl.right(t*30)
    tl.forward(l)
    dibuixar_triangle(c)
    tl.penup()
    tl.goto(0, 0)




def main() -> None:
    h = read(int)
    m = read(int)
    
    tl.hideturtle()
    tl.speed(0)

    dibuixa_rellotge(200, 50)
    dibuixar_busca(h, 90, 25)
    dibuixar_busca(m, 140, 25)
    tl.done()

if __name__ == "__main__":
    main()
