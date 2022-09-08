from yogi import read

n = read(int)

num = []

for i in str(n):
    num.insert(0, i)

print("".join(num))
