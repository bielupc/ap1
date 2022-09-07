from yogi import read

y = read(int)

if ((y % 4) == 0 and str(y)[-2:] != "00") or (str(y)[-2:] == "00" and int(str(y)[:-2]) % 4 == 0):
    print("YES")
else:
    print("NO")
