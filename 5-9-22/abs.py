from yogi import read

x = read(int)

if x < 0:
    x = -x
print(x)
