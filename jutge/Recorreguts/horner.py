from yogi import tokens, scan, read


def main() -> None:
    
    x = read(float)
    cn = scan(float)
    cn_prev = scan(float)

    while cn is not None and cn_prev is not None:
        cn = cn * x + cn_prev
        cn_prev = scan(float)
    if cn is not None:
        print("{:.4f}".format(cn))
            
if __name__ == "__main__":
    main()
