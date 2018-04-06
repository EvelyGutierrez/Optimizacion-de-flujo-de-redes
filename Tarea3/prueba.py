from grafo2 import Grafo
from datetime import datetime
instanteInicial = datetime.now()
print("GRAFO 1")
G1 = Grafo()
G1.creaNodos(20)
G1.imprimir("prueba.txt")
E = G1.conecta(0.6)
print("tamanno de E")
print(E)
G1.grafica("prueba.plot")
d = G1.FloydWarshall()
#print("Valor de d ")
#print(d)
a = G1.FordFulkerson(1,19)
print("Tiempo")
# al final de la partida
instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
segundos = tiempo.seconds
print(segundos)


#G1.test(1,19)
print("FordFulkerson desde el inicio hasta n ")
print(a)

#Prueba para otro grafo del mismo o distinto tamanno

print("GRAFO 2")
G2 = Grafo()
G2.creaNodos(30)
G2.imprimir("prueba.txt")
E = G2.conecta(0.6)
print("tamanno de E")
print(E)
G2.grafica("prueba.plot")
#print(prueba.FloydWarshall())
d = G2.FloydWarshall()
#print("Valor de d ")
#print(d)
#a = G2.FordFulkerson(1,19)
#tiempo = G2.TiempoEjecucion()
print("Tiempo")
print("FordFulkerson desde el inicio hasta n ")
print(a)

