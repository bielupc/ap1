from yogi import read

n = read(int)
d = 0
if n == 0:
    d = 1
else:
    while n != 0: 
        d += 1
        n = n // 10
print(d)


# sense el cas 0 explícit
