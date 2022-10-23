from yogi import scan, read, tokens
from math import pi

n = read(int)

for i in range(n):
    type = read(str)

    if type == "rectangle":
        l = read(float)
        w = read(float)
        print("{:.6f}".format(l * w))

    else:
        r = read(float)
        print("{:.6f}".format(pi * r**2))


