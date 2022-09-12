from yogi import read


n = read(int)

i = 1

while i*i <= n:
    if n % i == 0:
        print(i, n // i)
    i += 1
if i*i == n:    #soluciona el problema del quadrat perfecte
    print(i)


# Quan trobes un divisor en trobes dos si aquest pertany a l'interval inferior de l'arrel de n
# N inclouen el 0 en informàtica

# Sense l'optimització el cost es lineal, ara és arrel de n
