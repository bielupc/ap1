from dataclasses import dataclass
from time import sleep

@dataclass
class Pellicula:
  identificador: int
  titol: str
  director: str
  year: int
  blanc_i_negre: bool

p1 = Pellicula(1001, "Star Wars IV", "George Lucas", 1977, False)
p2 = Pellicula(1234, "The Kid", "Buster Keaton", 1921, True)

print(p1.any)

p2.director = "Charlie Chaplin"


@dataclass
class Hora:
  h: int = 0
  m: int = 0
  s: int = 0

migdia = Hora(12, 0, 0)
mitjanit = Hora(0, 0, 0)

alarma = Hora(s=0, m=30, h=7)
alarma = Hora(7, 30)

def escriure_hora(hora: Hora) -> None:
  print(f"{hora.h:02d}:{hora.m:02d}:{hora.s:02d}")

def incrementar_un_segon(hora: Hora) -> None:
    hora.s += 1
    if hora.s == 60:
        hora.s = 0
        hora.m += 1
        if hora.m == 60:
            hora.m = 0
            hora.h += 1
            if hora.h == 24:
                hora.h = 0

def un_segon_mes_tard(hora: Hora) -> Hora:
    despres = dataclasses.replace(hora)
    despres.s += 1
    if despres.s == 60:
        despres.s = 0
        despres.m += 1
        if despres.m == 60:
            despres.m = 0
            despres.h += 1
            if despres.h == 24:
                despres.h = 0
    return despres


def main() -> None:
    hora = Hora(23, 59, 55)
    alarma = Hora(7, 30)
    while True:
        escriure_hora(hora)
        if hora == alarma:
            print('ring ring!')
        sleep(1)                       # esperar un segon
        incrementar_un_segon(hora)

if __name__ == '__main__':
    main()

