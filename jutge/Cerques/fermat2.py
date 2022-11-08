from yogi import scan

def main() -> None:
    found = False 
    a = scan(int)
    b = scan(int)
    c = scan(int)
    d = scan(int)

    zero_i = False
    zero_j = False

    x = 0
    y = 0

    while a is not None and b is not None and c is not None and d is not None and not found:
        
        for i in range(a, b+1):
            if i == 0:
                zero_i = True
                break
            else:
                zero_i = False
                break

        for j in range(c, d+1):
            if j == 0:
                zero_j = True
                break
            else:
                zero_j = False
                break

        if zero_j or zero_i:

            found = True
            print("0^3 + 0^3 = 0^3")
            break


        a = scan(int)
        b = scan(int)
        c = scan(int)
        d = scan(int)

    if not found:
        print("No solution!")

if __name__ == "__main__":
    main()









