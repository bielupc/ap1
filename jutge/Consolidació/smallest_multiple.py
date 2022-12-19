from yogi import read, scan, tokens


def main():
  i = 1
  a = scan(int)

  while a is not None:
    b = scan(int)
    d = a
    while True:
      if d % b == 0:
        print(f"#{i} : {d}")
        break
      else:
        d += 1
    i += 1
    a = scan(int)


if __name__ == "__main__":
  main()