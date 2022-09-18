from yogi import read



# al fer l'append si esta duplicat el borra

n = read(int)

def is_prime(num):
    d = 1
    while d*d < num:
        if n % d == 0:
            if d != 1 and d != num:
                return False
    d += 1
    if d * d == num:
        if d != 1 and d != num:
            return False

    return True



def find_prime_divisors(n):

    primes = []
    d = 1

    while d*d < n:
     if n % d == 0:
        if is_prime(d) == True:
             primes.append(d)
            
        if is_prime(n//d) == True:
            primes.append(n//d)
     d += 1
     if d * d == n:
        primes.append(d)
    return primes 


print(find_prime_divisors(n))


#for num in divisors:
 #       aux = n
 #       while aux % num == 0:
 #           print(num)
 #           aux //= num


