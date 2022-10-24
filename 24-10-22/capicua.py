

def capicua(L: list[int]) -> bool:
    """Indica si L és cap i cua"""
    # return L == list(reversed(L))
    
    n = len(L)
    for i in range(n//2):
        if L[i] != L[n - 1 - i]:
            return False
    return True

def main() -> None:
    L = [5, 2, 1, 1, 2, 5]
    print(capicua(L))


if __name__ == "__main__":
    main()
