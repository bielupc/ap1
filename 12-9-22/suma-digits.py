from yogi import read

n = read(int)
d = 0
while n != 0: 
        d += n % 10
        n = n // 10
print(d)


