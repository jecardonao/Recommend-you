matriz = [[1, 2, 2, 2, 3, 4], [1, 2, 3, 3, 4, 5], [3, 4, 4, 4, 4, 6], [4, 5, 6, 7, 8, 9]]

for e in matriz:
    print(e)
a = int(input("Ingrese el numero a buscar en la matriz"))


def busquemos(x, y):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == y:
                return True
    return False


def quees(x):
    if x:
        print("Si")
    else:
        print("No")


quees(busquemos(matriz, a))