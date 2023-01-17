from yogi import read, scan, tokens

def jaccard(A: list[int], B: list[int]) -> float:
  if len(A) < len(B):
    A, B = B,A
  I = [x for x in B if x in A]
  return len(I) / (len(A) + len(B) - len(I))

def main() -> None:
  m1 = scan(int)
  while m1 is not None:
    A: list[int] = list()
    B: list[int] = list()
    for _ in range(m1):
      n = read(int)
      A.append(n)
    m2 = read(int)
    for _ in range(m2):
      n = read(int)
      B.append(n)
    print("{:.3f}".format(jaccard(A, B))) 
  m1 = scan(int)
    

if __name__ == "__main__":
  main()