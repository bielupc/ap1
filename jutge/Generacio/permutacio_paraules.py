from yogi import read, tokens, scan


def generar_permutacions(n: int, words: list[str]) -> None:

    L = ["" for _ in range(n)]
    usats = ["" for _ in range(n)]
    generar_permutacions_rec(usats, n, words, L, 0)

def generar_permutacions_rec(usats: list[str], n: int, words: list[str], L: list[str], i: int) -> None:

   if n == i:
      print("(", ','.join([str(x) for x in L]), ")", sep="")

   else:
      for word in words:
         if i == 0 or word not in usats:
            L[i] = word
            usats[i] = word
            generar_permutacions_rec(usats, n, words, L, i+1)
            usats[i] = ""





def main() -> None:
   n = read(int)

   words = [read(str) for _ in range(n)]
   generar_permutacions(n, words)


if __name__ == "__main__":
    main()
