import os, sys
#import networkx as nx
from GrafoTarea4 import Grafo
import collections as col


print("-------------------GRAFOS------------------")

n = 10
k = 5
G1 = Grafo()    
G1.creaNodos(n)
G1.imprimir("prueba.txt")


#avgdist = G1.avgdist()
#print(avgdist)
xn = G1.GuardaCirculo("circulo.txt",k, n, 0.5, 0.5, 0.1, 0.5)
print(xn)
G1.PlotCirculo("circulo.plot","circulo.txt")
G1.Grafica("aristas.plot")
   


print("------------------------------------")

a = G1.ver()
print(a)

