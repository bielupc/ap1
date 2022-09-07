from yogi import read

t = read(int)

if t > 30:
    print("it's hot")

    if t >= 100:
        print("water would boil")

elif t < 10:
    print("it's cold")

    if t <= 0:
        print("water would freeze")

else:
    print("it's ok")

