from yogi import tokens, read

def main() -> None:
    i = read(int)
    j = 1

    for n in tokens(int): 
        if i == j:
            print(f"At the position {i} there is a(n) {n}.")
            break
        else:
            j += 1

if __name__ == "__main__":
    main()
