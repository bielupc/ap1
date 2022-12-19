from yogi import read, tokens, scan




def main() -> None:

    L = [x for x in tokens(str)]


    maxim = L[0]
    segon_maxim = L[0]
    minim = L[0]


    for w in L:
        if w <= maxim:
            maxim = w
        if w <= segon_maxim:
            segon_maxim = w
    print(segon_maxim)




if __name__ == "__main__":
    main()
