llista = [1, 2, 3, 4, 5]

print(llista[-1]) # Ultim element de la llista

llista[2] = 99 # Modificar element de la llista

llista = list(range(10))

print(llista[2:6]) # De la posició 2 a la 6 sense incloure (2, 5)
print(llista[2:]) # Del valor al final
print(llista[:2]) # Del principi fins al dos
print(llista[:]) # Subllista tot
print(llista[2:8:2]) # De dos en dos range(2, 8, 2)

print(llista[::-1]) # .reverse


llista.append(9) # Afegir 9 pel final
llista.insert(4, 99) # Afegir a la pos 4 el 99
llista.pop() # Elimina últim element i retorna aquest element
llista.pop(3) # Elimina element de la posicio 3
del llista[3]

l1 = [1, 2, 3]
l2 = [3, 4, 5]

l1 + l2 # Concatenar
l1.extend(l2) 
l2 * 6 # 3,4,6 sis cops
l2 * 0 # llista buida
l1.clear()

"joan" not in["pep", "ana", "berta"]


for x in llista:
    print(x)

print(x for x in llista)

for i in range(len(llista)):
    llista[i] *= 2



