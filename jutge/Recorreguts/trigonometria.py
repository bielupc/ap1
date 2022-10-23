from math import *
from yogi import tokens 

for number in tokens(float):
    print("{:.6f}".format(sin(radians(number))), end=" ")
    print("{:.6f}".format(cos(radians(number))))
