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
    provincies: list[Provincia]
    

Paisos: TypeAlias = list[Pais]

def habitants(paisos: Paisos, x: float) -> int:
  habitants = 0
  for pais in paisos:
    count = 0
    for provincia in pais.provincies:
      if provincia.pib <= x:
        count += 1

      if count >= 2:
        habitants += provincia.habitants