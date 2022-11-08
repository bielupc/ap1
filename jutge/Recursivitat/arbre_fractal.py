import turtle as tl
from yogi import read

def dibuixar_arbre(n: int, d: float, a: int) -> None:
    if n == 1:
        tl.forward(d)
        tl.backward(d)
    else:
        tl.forward(d)
        tl.left(a)
        dibuixar_arbre(n-1, 3/4 * d, a)
        tl.right(2*a)
        dibuixar_arbre(n-1, 3/4 * d, a)
        tl.left(a)
        tl.backward(d)

    

def main() -> None: 
    n = read(int)
    d = read(float)
    a = read(int)

    tl.hideturtle()
    tl.speed(0)
    tl.left(90)
    dibuixar_arbre(n, d, a)
    
    tl.done()

    

if __name__ == "__main__":
    main()
