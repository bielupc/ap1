
def is_increasing(n: int) -> bool:
    if n < 10:
        return True
    elif n%10 >= (n//10)%10:
        return is_increasing(n//10)
    else:
        return False

