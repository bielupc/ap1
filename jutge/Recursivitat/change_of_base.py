from yogi import scan





def convert(n: int, b: int) -> str:
    if n == 0:
        return ""
        
    else:
        if b == 16:
            digit = n%b
            end = ""

            if digit == 10:
                end = "A"
            elif digit == 11:
                end = "B"
            elif digit == 12:
                end = "C"
            elif digit == 13:
                end = "D"
            elif digit == 14:
                end = "E"
            elif digit == 15:
                end = "F" 
            else:
                end = str(digit)

            return convert(n//b, b) + end 

        else:
            return convert(n//b, b) + str(n%b)

def main() -> None:
    n = scan(int)
    while n is not None:
        if n == 0:
            print("0 = 0, 0, 0")
            n = scan(int)
        else:
            print(f"{n} = {convert(n, 2)}", end=", ")
            print(convert(n, 8), end=", ")
            print(convert(n, 16))
            n = scan(int)
            
    

if __name__ == "__main__":
    main()


