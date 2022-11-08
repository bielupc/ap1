
def is_prime(n: int) -> bool:
    """Returns if a natural number n >= 0 is prime"""
    if n <= 1:
        return False
    else:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            else:
                d += 1
        return True

def sum_of_digits(n: int) -> int:
    """Returns the sum of digits of a natural n >= 0"""

    if n < 10:
        return n
    else:
        return n%10 + sum_of_digits(n//10)

def is_perfect_prime(n: int) -> bool:
    """Given a natural number n, returns if it's a perfect prime"""
    return (n < 10 or is_prime(sum_of_digits(n))) and is_prime(n)


