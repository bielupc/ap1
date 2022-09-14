from yogi import read
import turtle as tl

n = read(int)
m = read(int)


for i in range(1, n+1):
    tl.forward(i * m)
    tl.left(90)
    tl.forward(i * m)
    tl.left(90)



tl.done()

