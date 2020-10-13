import pandas as pd
import numpy as np

file = pd.read_csv('lite.cvs', sep=';')


def separador(x):
    a = np.matriz(x.values)
    for i in range(len(a)):
        s = a[i, 18]
        s = s[-4:]
        p = a[i, 19]
        p = p//10
        a[i, 18] = int(p)-int(s)
        if a[i, 1] == 'no':
            a[i, 1] == 00
    a1 = np.delete(a, [0, 11, 12, 22, 24, 48, 50, 57, 58, 62, 64], 1)
    return a1


print(separador(file)[:, -1].transpose().tolist[0])
print(separador(file)[:, :-1].tolist())

x = separador(file)[:, :-1].tolist()
y = separador(file)[:, -1].transpose().tolist[0]
