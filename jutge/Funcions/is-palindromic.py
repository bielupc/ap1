from yogi import read

def is_palindromic(n:int) -> bool:
    """Retorna en forma de boolea si n es is_palindromic"""
    length = len(n)
    if length == 1:
        return True

    for i in range(1, length + 1):
        if n//(10**i) == n%(10**i):
            print("True", n//(10**i), n%(10**i))


n = read(int)
is_palindromic(n)
