import os, sys
#import networkx as nx
from GrafoTarea4 import Grafo
import collections as col
from datetime import datetime
from time import clock
print("-------------------GRAFOS------------------")
n = 200
k = 1
r = 0.5
p = 0.0000000002
entro1 = True
entra = True

cantidadCorridas = 10
if(entro1 != False):
    with open("TiempoFWTarea4.txt", "a") as f:


        for t in range(cantidadCorridas):
            
            G1 = Grafo()    
            G1.creaNodos(n)
            G1.imprimir("prueba.txt")


            xn = G1.GuardaCirculo("circulo.txt",k, n, p, r, 0.1, 0.5)
            #print(xn)
            G1.PlotCirculo("circulo.plot","circulo.txt")
            G1.Grafica("aristas.plot")

            Inicialavgdist = clock() # Tiempo Inicial avgdist
            avgdist = G1.avgdist()
            print("Funcion avgdist   ---------------------------------------")
            print(avgdist)

            print("Resultado de avgdist en tamanno del conjunto :")
            print(avgdist)
                    
            tiempoavgdist = clock() - Inicialavgdist
            print("Tiempo de ejecucion avgdist: ")
            print(tiempoavgdist)

            Inicialclustcoef = clock() # Tiempo Inicial clustcoef
            clustcoef = G1.clustcoef2()
            print("Funcion clustcoef   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(clustcoef)
            tiempoclustcoef = clock() - Inicialclustcoef
            print("Tiempo de clustcoef: ")
            print(tiempoclustcoef)
            cotaSuperior = G1.cota(n, k, r)
            print(cotaSuperior)
            #p = p + 0.0000000001
            k = k + 1
            n = n + 5
            print("---------------------------------------------------------" + str(t))
            print("Valores de N mas 10 :")
            print(n)         
            
            f.write('{}, {}, {} \n'.format(n, tiempoavgdist, tiempoclustcoef))        


if(entro1 != False):
    G1.PlotDiagrama1("diagrama2.plot", "TiempoFWTarea4")

if(entra != False):

    print("-------------------GRAFOS Prob------------------")
    n = 50
    k = 4
    r = 0.5
    p = 0.0000000002
    Resultadosavgdist = []
    Resultadosclustcoef = []
    cantidadCorridas = 100
    with open("ProbTarea4.txt", "a") as f:
    # para las pruebas del grafico de distancias contra densidad variando p

        for t in range(cantidadCorridas):
            
            G1 = Grafo()    
            G1.creaNodos(n)
            G1.imprimir("prueba.txt")


            xn = G1.GuardaCirculo("circulo.txt",k, n, p, r, 0.1, 0.5)
            #print(xn)
            G1.PlotCirculo("circulo.plot","circulo.txt")
            G1.Grafica("aristas.plot")

            
            avgdist = G1.avgdist()
            print("Funcion avgdist   ---------------------------------------")
            print(avgdist)
            Resultadosavgdist.append(avgdist)
            print("Resultado de avgdist en tamanno del conjunto :")
            print(avgdist)
                    
           
          

            
            clustcoef = G1.clustcoef2()
            print("Funcion clustcoef   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(clustcoef)
            Resultadosclustcoef.append(clustcoef)
            
            cotaSuperior = G1.cota(n, k, r)
            print(cotaSuperior)
              
            p = p + 0.0000000001
            print("---------------------------------------------------------" + str(p))
            print("Valores de N mas 10 :")
            print(n)         
            
            f.write('{}, {}, {} \n'.format(n, avgdist,clustcoef))        

print(Resultadosavgdist)
print(Resultadosclustcoef)

if(entra != False):
    G1.PlotDiagrama2("diagrama1.plot", "ProbTarea4")

