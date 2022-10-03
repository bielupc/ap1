from yogi import scan, read, tokens

m = read(int)

for x in tokens(int):
    if x > m:
        m = x
print(m)
