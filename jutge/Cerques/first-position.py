from yogi import tokens


def main() -> None:
    i = 0
    for n in tokens(int):
        i += 1
        if n % 2 == 0:
            print(i)
            break

if __name__ == "__main__":
    main()


