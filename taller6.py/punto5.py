listaA= [1,2,2,3,1,2,3,1,2,3,1,2,3,1,1,3]
listaA.sort()
mayor = listaA[0]
c = votos = listaA.count(mayor)

for i range(c,len(listaA)):
    if votos < listaA.count(listaA[i]):
        mayor = listaA[i]
        votos = listaA.count(mayor)
print("El ganador es", mayor,"Votos", votos)
