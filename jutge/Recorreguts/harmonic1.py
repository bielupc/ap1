from yogi import read

def main() -> None:
    n = read(int)
    har = 0.0
    for i in range(1, n+1):
        har += 1/i
    print("{:.4f}".format(har))

if __name__ == "__main__":
    main()






