lista = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]
auxiliar = []

for i in range(0, len(lista)):
    if lista[i] not in auxiliar:
        auxiliar.append(lista[i])

lista = auxiliar
print(lista)