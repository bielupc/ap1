from yogi import read, scan, tokens

x = read(float)
exp = 0
res = 0.0

for coef in tokens(float):
    res += coef * x**exp
    exp += 1

print("{:.4f}".format(res))


