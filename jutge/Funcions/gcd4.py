
def gcd(a:int, b:int) -> int:
    """Troba el MCD de dos nombres > 0 i almenys un d'ells != 0"""
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def gcd4(a:int, b:int, c:int, d:int) -> int:
    """Troba el MCD de 4 nombres > 0"""
    n = gcd(a, b)
    m = gcd(c, d)

    return gcd(n, m)




