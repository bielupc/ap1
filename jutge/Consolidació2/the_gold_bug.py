from yogi import read, scan, tokens
from typing import Union, List


def main() -> None:
  alphabet  = "abcdefghijklmnopqrstuvwxyz"
  translation_table = [char for char in scan(str)]

  while translation_table is not None:
    n = read(int)
    for _ in range(n):
      line = read(str)
      for char in line:
        if char == "_":
          print(" ", end="")
        else:
          print(alphabet[translation_table.index(char)], end="")
      print()
      
    print()
    translation_table = scan(str)


if __name__ == "__main__":
  main()