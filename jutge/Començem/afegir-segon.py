from yogi import read

h = read(int)
m = read(int)
s = read(int)


s = s+1

if s == 60:
    s = 0
    m = m+1

    if m == 60:
        m = 0
        h = h+1
        if h == 24:
            h = 0

hora = [h, m, s]
output = ["%02d" % n for n in hora]

print(":".join(map(str, output)))
