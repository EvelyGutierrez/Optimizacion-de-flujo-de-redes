from grafo2 import Grafo
from datetime import datetime
from time import clock

print("-------------------GRAFOS------------------")

n = 30
p = 0
resultadosFF = []
cantidadCorridas = 30
with open("tiemposFFyFW.txt", "a") as f:
 
    for t in range(cantidadCorridas):
        G1 = Grafo()    
        G1.creaNodos(n)
        G1.imprimir("prueba.txt")
        E = G1.conecta(0.6)    
        G1.grafica("prueba.plot")
        InicialFloyd = clock() # Tiempo Inicial FloydWarshall
        d = G1.FloydWarshall()
        print("Resultado de FloydWarshall en tamanno del conjunto :")
        print(d)
        
        tiempoFloyd = clock() - InicialFloyd
        print("Tiempo de ejecucion FloydWarshall: ")
        print(tiempoFloyd)
        
        
        InicialFord = clock()# Tiempo Inicial FordFulkerson
        a = G1.FordFulkerson(1,n - 1)
        FinalFord = clock() #Tiempo Final
        tiempoFord = clock() - InicialFord # Devuelve un objeto timedelta
        print("Tiempo de ejecucion FordFulkerson: ")
        print(tiempoFord)
        print("FordFulkerson desde el inicio hasta n - 1 ")
        print(a)
        p = p + 1
        n = n + 5
        print("---------------------------------------------------------" + str(p))
        print("Valores de N mas 10 :")
        print(n)
        
        resultadosFF.append(a)
        f.write('{}, {}, {} \n'.format(n, tiempoFloyd, tiempoFord))

print("Flujos Maximos por corridas: ")
print(resultadosFF)



