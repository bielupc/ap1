from yogi import read, scan, tokens



def is_palindrome(s: str) -> bool:
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


def main() -> None:
    s = "0012310012"
    print(is_palindrome(s))

if __name__ == "__main__":
    main()
