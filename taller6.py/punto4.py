def Shell(lista):
     contador = len(lista)//2
while contador > 0:
    for inicio in range(contador):
     brecha(lista,inicio,contador)
     print(contador)
    contador = contador// 2

def brecha(lista,inicio,brecha):
    for i in range(inicio+brecha,len(lista),brecha):

        valorActual = lista[i]
        posicion = i

        while posicion>=brecha and lista[posicion-brecha]>valorActual:
            lista[posicion]=lista[posicion-brecha]
            posicion = posicion-brecha

        lista[posicion]=valorActual

lista = [8,43,17,6,40,16,18,97,11,7]
Shell(lista)
print(lista)
