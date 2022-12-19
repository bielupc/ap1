from yogi import read, scan


def moda(counted: list[tuple[str, int]]):
    print(counted)
    stored_max = -1 
    word_max = ""
    for item in counted:
        if item[1] > stored_max:
            stored_max = item[1]
            word_max = item[0]
        elif item[1] == stored_max:
            word_max = max(item[0], word_max)
    return word_max

def main() -> None:
    n = read(int)

    while n != 0:
        words: list[str] = list()
        for _ in range(n):
            words.append(read(str))
        words.sort()

        counted: list[tuple[str, int]] = list()

        count = 1
        for i in range(len(words)):
            if i == 0:
                counted.append((words[i], count))
                pass


            else:
                if words[i] == words[i-1]:
                    count += 1
                else:
                    counted.append((words[i], count))
                    count = 1
            print(moda(counted))
        n = read(int)


if __name__ == "__main__":
    main()
