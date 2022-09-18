import turtle
size = 50
for x in range(-300//size, 300//size):
    for y in range(-300//size, 300//size):
        turtle.up()
        turtle.goto(x * size, y * size)
        turtle.down()
        for sides in range(4):
            turtle.forward(size)
            turtle.left(90)
turtle.update()
turtle.done()
 
