from yogi import *

pics = 0

a = scan(int)
if a is not None:
    b = scan(int)
    if b is not None:
        c = scan(int)
        while c is not None:
            if a < b > c:
                pics += 1
            a, b, c = b, c, scan(int)
    print(pics)
