def negativos(lista):
    resul = []
    for elem in lista:
        if elem < 0:
            resul.append(elem)
    return resul


n = int(input("Cuantos elementos va a ingresar: "))
a = []
for i in range(n):
    x = int(input("Numero: "))
    a.append(x)

Lista = negativos(a)
print(Lista)