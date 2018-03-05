from grafo2 import Grafo
prueba = Grafo()
prueba.creaNodos(5)
prueba.imprimir("prueba.txt")
prueba.conecta(0.6)
prueba.grafica("prueba.plot")
print(prueba.floyd_warshall())
a = prueba.ford_fulkerson(2,3)
print(a)
