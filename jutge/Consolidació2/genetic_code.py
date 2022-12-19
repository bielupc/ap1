from yogi import read, tokens, scan

def trobar_cadena(inici: bool, stop: bool, cadena: str) -> tuple[bool, bool, str]:

  # trobem l'inici de la seqüència de codons
  if not inici:
    for i in range(1, len(cadena)-1):
      if cadena[i-1] + cadena[i] + cadena[i+1] == "AUG":
        bases = cadena[i+2:]
        inici = True
        break
  if not inici:
    return False, False, "NO"
  else:
      # busquem els codons de stop
      codons = [bases[i:i+3] for i in range(0, len(bases), 3)]

      i = 0
      for codon in codons:
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
          codons = codons[:i]
          stop = True
          break
        i += 1

      # convertim cada codon a una proteina
      res = ""
      for codon in codons:
        if codon[0] == "U":
          if codon[1] == "U":
            if codon[2] == "U" or codon[2] == "C":
              res += "Phe"
            else:
              res += "Leu"
          elif codon[1] == "C":
            res += "Ser"
          elif codon[1] == "A":
            res += "Tyr"
          else:
            if codon[2] == "U" or codon[2] == "G":
              res += "Cys"
            else:
              res += "Trp"

        elif codon[0] == "C":
          if codon[1] == "U":
            res += "Leu"
          elif codon[1] == "C":
            res += "Pro"
          elif codon[1] == "A":
            if codon[2] == "U" or codon[2] == "C":
              res += "His"
            else:
              res += "Gln" 
          else:
            res += "Arg"

        elif codon[0] == "A":
          if codon[1] == "U":
            if codon[2] == "G":
              res += "Met"
            else:
              res += "Ile"
          elif codon[1] == "C":
            res += "Thr"
          elif codon[1] == "A":
            if codon[2] == "U" or codon[2] == "C":
              res += "Asn"
            else:
              res += "Lys"
          else:
            if codon[2] == "U" or codon[2] == "C":
              res += "Ser"
            else:
              res += "Arg"

        else:
          if codon[1] == "U":
            res += "Val"
          elif codon[1] == "C":
            res += "Ala"
          elif codon[1] == "G":
            res += "Gly"
          else:
            if codon[2] == "G" or codon[2] == "A":
              res += "Glu"
            else:
              res += "Asp"
      return True, stop, res 


def main() -> None:
  gen = read(str)
  while gen[-1] != ":":
    gen = read(str)
  
  # llegim la cadena
  stop = False
  inici = False
  linia = scan(str)

  while linia is not None and not stop:
    print(linia)
    _, stop, cadena = trobar_cadena(inici, stop, linia)

    if cadena != "NO":
      print(cadena)

    linia = scan(str)



if __name__ == "__main__":
  main()