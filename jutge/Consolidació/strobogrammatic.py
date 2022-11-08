from typing import Optional
from yogi import tokens 


def llargada(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + llargada(n//10)

def strobogrammatic(n: int) -> Optional[int]:
    strobo_str = ""

    for i in range(llargada(n)):
        strobo_str += str(n%10)
        n //= 10
    
    out = ""
    for char in strobo_str:
        if char == "6":
            out += "9"
        elif char == "9":
            out += "6"
        elif char == "0" or char == "1" or char == "8":
            out += char
        else:
            return None 
    return int(out)


def main() -> None:
    odds = 0
    for i in tokens(int):
        n = strobogrammatic(i)
        if n is not None:
            if n == i:
                if n%2 != 0:
                    odds += 1
                print(f"{i} is strobogrammatic")
            else:
                print(f"{i} is not strobogrammatic")
        else:
            print(f"{i} is not strobogrammatic")
    print()
    print(f"odd strobogrammatic: {odds}")
    


if __name__ == "__main__":
    main()
