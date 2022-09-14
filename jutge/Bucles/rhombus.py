from yogi import read

n = read(int)
lines = (2 * n) - 1


for i in range(lines):
    for j in range(lines):
        print("*", end="")
    print()


