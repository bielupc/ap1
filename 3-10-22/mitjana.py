from yogi import scan

# python mitjana.py < dades.txt
# control + d no hi ha més dades, retorna None
# buffer


n = 0
s = 0.0

x = scan(float)

while x is not None:
    s = s + x
    n = n + 1
    x = scan(float)
print(s / n)
