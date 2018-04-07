from grafo2 import Grafo
from datetime import datetime
instanteInicial = datetime.now()# Tiempo Inicial 
print("-------------------GRAFOS------------------")

n = 20
tiempoTotal = []
cantidadCorridas = 10

for t in range(cantidadCorridas):
    G1 = Grafo()    
    G1.creaNodos(n)
    G1.imprimir("prueba.txt")
    E = G1.conecta(0.6)
    print("tamanno de E (conjunto de conexiones): ")
    print(E)
    G1.grafica("prueba.plot")
    d = G1.FloydWarshall()
    print("Resultado de FloydWarshall en tamanno del conjunto :")
    print(d)
    a = G1.FordFulkerson(1,n - 1)
    # al final de la partida
    instanteFinal = datetime.now() #Tiempo Final
    tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
    segundos = tiempo.seconds
    print("FordFulkerson desde el inicio hasta n - 1 ")
    print(a)
    
    n = n + 10
    print("Valores de N mas 10 :")
    print(n)
    tiempoTotal.append(segundos)
    
print(tiempoTotal)
