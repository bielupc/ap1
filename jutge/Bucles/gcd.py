from yogi import read


a = read(int)
b = read(int)

n = a
m = b


while b != 0:
    r = a % b
    a = b
    b = r
print(f"The gcd of {n} and {m} is {a}.")


