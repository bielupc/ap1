from yogi import read

a1 = read(int)
a2 = read(int)

b1 = read(int)
b2 = read(int)


if a1 == b1 and a2 == b2:
    print("=")

elif b1 <= a1 and b2 >= a2:
    print("1")

elif a1 <= b1 and a2 >= b2:
    print("2")
else:
    print("?")
