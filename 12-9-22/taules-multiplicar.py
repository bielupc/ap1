from yogi import read


i = 0 

while i <= 10:
    print("taula del", i)
    j = 0
    while j <= 10:
        print(i, "*", j, "=", i*j)
        j += 1
    print()
    i += 1 
