

def reduction_of_digits(x: int) -> int:
    if x < 10:
        return x
    else:
        return reduction_of_digits(x%10 + reduction_of_digits(x // 10))

