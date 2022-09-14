from yogi import read


a = read(int)
b = read(int)


d = min(a, b)

for i in range(1, d + 1):
    if a % d == 0 and b % d ==0:
        print(f"The gcd of {a} and {b} is {i}.")
        break
