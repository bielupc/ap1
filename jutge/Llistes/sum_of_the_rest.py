from yogi import read, scan, tokens


def sum_of_the_rest(n: int):
    L: list[int] = list()
    for _ in range(n):
        L.append(read(int))

    calculated: list[int] = list()
    sums = [sum([L[i] for i in range(n) if i != j]) for j in range(n) ]

    for i in range(n):
        if L[i] in calculated:
            continue
        elif L[i] in sums:
            return True
        calculated.append(L[i])
    return False


def main() -> None:
    n = scan(int)
    while n is not None:
        if n == 1:
            x = read(int)
            if x == 0:
                print("YES")
            else:
                print("NO")
        else:
            if sum_of_the_rest(n): 
                print("YES")
            else:
                print("NO")
        n = scan(int)

if __name__ == "__main__":
    main()