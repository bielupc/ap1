from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Provincia:
  nom: str
  capital: str
  habitants: int
  area: int
  pib: float

@dataclass
class Pais:
  nom: str
  capital: str
  provincies: list[provincies]


def habitants_totals(paisos: Paisos) -> int:
  h = 0
  for pais in paisos:
    for provincia in pais.provincies:
      h += provincia.habitants
