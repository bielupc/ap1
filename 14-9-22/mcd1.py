from yogi import read

a = read(int)
b = read(int)



while a != b:
    if a > b:
        a = a-b
    else:
        b = b-a

print(a)




# Si els dos nombres són iguals, ja el tens. Sinó, resta el més petit al més gran.

# mcd(a,a) = a
# mcd (a, b) = mcd(a-b, b) si a>b
