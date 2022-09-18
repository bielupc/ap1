from yogi import read

n = read(int)
lines = (2 * n) - 1

for i in range(1, n+1):
    print(" " * (n - i) + "*" * ((2 * i) - 1))

for j in reversed(range(1, n)):
    print(" " * (n - j) + "*" * ((2 * j) - 1))

