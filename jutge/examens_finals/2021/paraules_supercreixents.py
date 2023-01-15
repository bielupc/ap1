from yogi import scan, read, tokens


def generar_combinacions(n: int, c: str, letters: list[str], i: int, L: list[str]) -> None:

  if len(L) == n:
    print(*L)
  else:
    L.append(letters[i+2])
    generar_combinacions(n, c, letters, i+2, L)





def main() -> None:
  letters = list("abcdefghijklmnopqrstuvwxyz")
  n = read(int)
  c = read(str)
  L = [c]
  generar_combinacions(n, c, letters, letters.index(c), L)



if __name__ == "__main__":
  main()