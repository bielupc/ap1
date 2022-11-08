from yogi import read


def main() -> None:
    w = read(str)
    next_w = read(str)
    wrong = ""
    found = False

    while next_w != "END":

        if found and w < wrong:
            print(w)
            print(wrong)
        else:

            if w < next_w:
                print(w)
            else:
                wrong = w
                found = True

        w = next_w
        next_w = read(str)

if __name__ == "__main__":
    main()
