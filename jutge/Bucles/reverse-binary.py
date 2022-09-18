from yogi import read

n =	read(int)


num = []

if n == 0:
    print("0")
else:
    i = n
    while i != 0:
        num.append(str(i % 2))
        i = i // 2

    print("".join(num))






