from yogi import read

x =	read(int)
y =	read(int)

if x > y:
    i =	x

    while i != y-1:
        print(i)
        i -= 1

else:
    i =	y
    while i != x-1:
        print(i)
        i -= 1	
