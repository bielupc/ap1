from yogi import tokens


def sumardigits(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + sumardigits(n // 10)





for number in tokens(int):
    print(f"The sum of the digits of {number} is {sumardigits(number)}.")
