row = int(input('Ingrese número de fila: '))
column = int(input('Ingrese número de columna: '))


def pascal(row, column):
     if row < 0 and column < 0:
         return 0
     elif row == 0:
        return 0
     elif column == 0:
         return 1
    else:         
        return (row * pascal(row-1, column-1)) / column 

print(pascal(row, column))
