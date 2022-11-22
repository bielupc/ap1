from yogi import tokens, scan, read

def main() -> None:
    for w in tokens(str):
        print(w[::-1])

if __name__ == "__main__":
    main()