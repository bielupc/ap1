

def escriure_factors_primers(n: int) -> None:
    if n == 1:
        print("")
       
    else:
        factors = []

        d = 2

        while d <= n:

            if n%d == 0:

                n //= d

                if d not in factors:
                    factors.append(d)
            else:
                d += 1

        
        print(",".join(map(str, factors)))


