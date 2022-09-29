from yogi import read

s = 0
n = read(int)
for i in range(n):
    x = read(float)
    s += x

print(s / n)

