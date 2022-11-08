from typing import Optional
from yogi import read, tokens

def main() -> None:
    i = read(int)
    print(index(i))

def index(i: int) -> Optional[str]:
    
    j = 1

    if i <= 0:
        return "Incorrect position."
    else:
        for n in tokens(int):
            if n is not None:
                if i == j:
                    return f"At the position {i} there is a(n) {n}."
                else:
                    j += 1
        if i > j-1:
            return "Incorrect position."
        else:
            return None

if __name__ == "__main__":
    main()



