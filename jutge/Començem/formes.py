from yogi import read
import turtle as tl

forma = read(str)

if forma == "cercle":
    radi = read(int)
    tl.circle(radi)
elif forma == "quadrat":
    costat = read(int)
    for i in range(4):
        tl.forward(costat)
        tl.left(90)

elif forma == "rectangle":
    costat = read(int)
    h = read(int)
    for i in range(2):
        tl.forward(costat)
        tl.left(90)
        tl.forward(h)
        tl.left(90)
tl.done()

