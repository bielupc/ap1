from yogi import read, scan



def main() -> None:
  n = read(int)
  m = read(int)


  M = [[read(int) for _ in range(m)] for _ in range(n)]
  q = scan(str)
  while q is not None:
    if q == "row":
      i = read(int) 
      print(f"row {i}:", *M[i-1])

    elif q == "column":
      idx = read(int) - 1

      col: list[int] = list()
      for i in range(n):
        for j in range(m):
          if j == idx:
            col.append(M[i][j]) 
      print(f"column {idx + 1}:", *col)

    else:
      i = read(int) 
      j = read(int)  

      print(f"element {i} {j}:", M[i-1][j-1])
      
        
    q = scan(str)


if __name__ == "__main__":
  main()