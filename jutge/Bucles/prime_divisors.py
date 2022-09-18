from yogi import read

n = read(int)

d = 1


while d*d != 0:
    if n % d == 0:
        print(d, n//d)
    d += 1

if d * d == n:
    print(d)



