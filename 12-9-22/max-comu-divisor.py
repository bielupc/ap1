from yogi import read

a = read(int)
b = read(int)


if a > b:
    d = b
else:
    d = a
while a % d != 0 or b % d != 0:
    d = d  - 1
print(d)
