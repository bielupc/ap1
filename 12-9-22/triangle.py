

n = 5

for i in range(n):
    for j in range(i+1):
        print("o", end="")
    print()


for j in range(n):
    print("o" * (i+1))
