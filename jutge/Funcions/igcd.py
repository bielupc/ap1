
def gcd(a:int, b:int) -> int:
    """Troba el MCD de dos nombres > 0 i almenys un d'ells != 0"""
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
