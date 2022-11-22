from yogi import read, tokens, scan
from typing import List

def print_freq(counts: list[int]) -> None:
    pos_max = 0
    max_count = counts[0]

    for digit, count in enumerate(counts): #(index, element)
        if count > max_count:
            pos_max = digit
            max_count = count

    print(pos_max, max_count)


def main() -> None:
    base = read(int)
    counts = [0 for _ in range(base)]
    n = scan(int)
    while n is not None:
        if n == 0:
            counts[0] += 1
        while n > 0:
            counts[n % base] += 1
            n = n // base
        n = scan(int)
    print_freq(counts)
    

if __name__ == "__main__":
    main()
