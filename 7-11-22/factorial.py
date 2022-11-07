def factorial(n: int) -> int:
    """Returns n!. Pre: n >= 0"""
    i = 0
    f = 1
    # Invariant: f = i! and i <= n

    while i != n:
        # f = i! and i < n
        i += 1
        f = f * i
        # f = i! and i <= n

    # f = i! and i <= n and i == n
    # f = n!
    return f


