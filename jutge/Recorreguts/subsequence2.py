from yogi import read, scan

paraula = scan(str)
llegida = scan(str)

ctl = 1
maxim = 1

while llegida is not None:

    if paraula == llegida:
        ctl += 1
        if ctl > maxim:
            maxim = ctl
    else:
        if ctl > maxim:
            maxim = ctl
        ctl = 0
        
    llegida = scan(str)

print(maxim)


