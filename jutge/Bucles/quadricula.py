import turtle as tl
from yogi import read

n = read(int)
m = read(int)

tl.hideturtle()


for i in range(n+1):
    tl.goto(0, (m*i))
    tl.down()
    tl.forward(n*m)
    tl.up()

tl.left(90)

for j in range(n+1):
    tl.goto((m*j), 0)
    tl.down()
    tl.forward(n*m)
    tl.up()





tl.done()



