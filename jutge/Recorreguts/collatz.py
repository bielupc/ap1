from yogi import tokens 


def main() -> None:

    for n in tokens(int):
        ctl = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1
            ctl += 1

        print(ctl)

if __name__ == "__main__":
    main()
