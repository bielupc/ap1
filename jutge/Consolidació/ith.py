from yogi import read, scan, tokens

def main() -> None:
    i = scan(int)
    j = 1
    trobat = False
    
    while i is not None:
        
        trobat = False
        for n in tokens(int):
            if n != -1:
                if j == i and not trobat:
                    print(f"At the position {i} there is a(n) {n}.")
                    trobat = True
                else:
                    j += 1

        if not trobat:
            print("Incorrect position.")
        
        i = scan(int)

        

if __name__ == "__main__":
    main()
