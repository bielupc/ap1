from yogi import read, tokens

def main() -> None:

    i = read(int)
    j = 1

    if i < 0:
        print("Incorrect position.")
    else:
        for n in tokens(int):
            if n == -1:
                print("Incorrect position.")
                break
            else:
                if i == j:
                    print(f"At the position {i} there is a(n) {n}.")
                    break
                else:
                    j += 1

if __name__ == "__main__":
    main()



