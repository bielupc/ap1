
def segon(b, c):
    return b, c

def primer(a, b, c):
    return a, segon(b, c)


print(primer(1,2,3))

print(type(primer(1, 2, 3)))
