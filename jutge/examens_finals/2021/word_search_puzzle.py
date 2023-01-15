from yogi import read, tokens, scan
from typing import TypeAlias, Union, TypeVar


def punts_max(p: str, t_lletres: list[list[str]], t_punts: list[list[int]]) -> int:
  """
  Retorna el nombre de punts màxims que es pot obtenir colocant la paraula al taulell.
  """
  return max(punts_horitzontals(p, t_lletres, t_punts), punts_verticals(p, t_lletres, t_punts))


def sumar_pos_horitzontal(i: int, j: int, p: str, t_lletres: list[list[str]], t_punts: list[list[int]], l: int) -> int:
  punts = 0
  for k in range(l):
    if p[k] == t_lletres[j][i+k]:
      punts += t_punts[j][i+k]
    else:
      punts = 0
  return punts
 

def punts_horitzontals(p:int, t_lletres: list[list[str]], t_punts: list[list[str]]) -> int:
  punts = 0
  r = len(t_lletres)
  c = len(t_lletres[0])
  l = len(p)

  for j in range(r):
    i = 0
    while i < (c-l) + 1:
      punts_pos = sumar_pos_horitzontal(i, j, p, t_lletres, t_punts, l)
      if punts_pos > punts:
        punts = punts_pos
      i += 1
  return punts


def sumar_pos_vertical(i: int, j: int, p: str, t_lletres: list[list[str]], t_punts: list[list[int]], l: int) -> int:
  punts = 0
  for k in range(l):
    if p[k] == t_lletres[j+k][i]:
      punts += t_punts[j+k][i]
    else:
      punts = 0
    return punts


def punts_verticals(p:int, t_lletres: list[list[str]], t_punts: list[list[str]]) -> int:
  punts = 0
  r = len(t_lletres)
  c = len(t_lletres[0])
  l = len(p)

  for i in range(c):
    j = 0
    while j < (r-l) +1:
      punts_pos = sumar_pos_vertical(i, j, p, t_lletres, t_punts, l)
      if punts_pos > punts:
        punts = punts_pos
      j += 1
  return punts


def main() -> None:
  r = scan(int)
  c = scan(int)

  while r is not None and c is not None:
    tauler_lletres = [[read(str) for j in range(c)] for i in range(r)]
    tauler_punts = [[read(int) for j in range(c)] for i in range(r)]
    t = read(int)
    for _ in range(t):
      paraula = read(str)
      punts = punts_max(paraula, tauler_lletres, tauler_punts)
      if punts != 0:
        print(punts)
      else:
        print("no")

    r = scan(int)
    c = scan(int)


if __name__ == "__main__":
  main()