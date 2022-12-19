from dataclasses import dataclass
from math import sqrt


@dataclass
class Punt:
    # x, y

@dataclass
class Rectancle
    # Punt(ie, sd)


@dataclass
class Cercle:
    # Punt c
    # radi

def dins_cercle(p: Punt, cercle: Cercle) -> bool:
    """----"""
    return dist(p, cercle.c) <= cercle.r

def dist(p: Punt, q: punt) -> float:
    """---"""
    return sqrt((p.x - q.x)**2 + (q.y - p.y)**2)

def rectancle_rectilini(cercle.Cercle) -> Rectancle:
    """---"""
    iex = cercle.x - cercle.r
    return Rectancle(Punt(iex, iey), Punt(sdx, sdy))

def translladar_rectangle(r: Rectancle,  dx: float, dy: float) -> None:
    """---"""
    r.iex.x += dx
    r.ie.y += dy
    r.sd.x += dx
    r.sd.y += dy

def punt_aleatori(r: Rectancle):
    """---"""
   px = (rand() / RAND_MAX) * (r.sd.x - r.ie.x)
    return Punt(px,py)

...

#rectangles contenidors de cada cercle, min(ie) max(sd)

