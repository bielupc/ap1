

def reverse_digits(n: int) -> int:
    """Prints n with reversed digits (base 10)
       Pre: n >= 0"""

    r = 0
    # Invariant gràfic
    while n != 0:
        r = 10 * r + n % 10
        n //= 10
    return r
