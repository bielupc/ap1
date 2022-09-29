from yogi import read

s  = 0.0
n = 0

x = read(str) 

while x != "fi":
    n += 1
    s += float(x)
    x = read(str)

print(s / n)
