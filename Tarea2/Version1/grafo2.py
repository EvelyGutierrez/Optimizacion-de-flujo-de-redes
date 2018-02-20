print("hola")
from random import random, choice
from sys import stdout

colores = ["black", "blue", "pink", "orange", "red"]

def cabecera(aristas, eps=False):
    if eps:
        print("set term postscript eps", file = aristas)
        print("set output 'grafo2.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'grafo2.png'", file = aristas)
    print("set xrange [-10.0:10.0]", file = aristas)
    print("set yrange [-10.0:10.0]", file = aristas)
    print('set size square', file = aristas) 
    print('set key off', file = aristas)

def pie(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 5".format(destino), file = aristas)

class Grafo:
    
    def __init__(self):
        self.n = None # se crean las variables pero aun no se inicializan
        self.x = dict()
        self.y = dict()
        self.E = []
        self.destino = None

    def creaNodos(self, orden): # creando los nodos
        self.n = orden
        for nodo in range(self.n):
            self.x[nodo] = random() * 10
            self.y[nodo] = random() * 10

    def imprimir(self, dest): # guardando los pares X y Y en un archivo
        self.destino = dest
        with open(self.destino , "w") as archivo:
            for nodo in range(self.n):
               print(self.x[nodo], self.y[nodo], file=archivo)
        print(self.destino)

    def conecta(self, prob):
        for nodo in range(self.n - 1):
            for otro in range(nodo + 1, self.n):           
                if random() < prob:
                    color = choice(colores)
                    self.E.append((nodo, otro, color))
        print(len(self.E))

    def grafica(self, plot): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            num = 1
            for (v, w, c) in self.E:
                x1 = self.x[v]
                x2 = self.x[w]
                y1 = self.y[v]
                y2 = self.y[w]
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 2 lt 5 lc rgb '{:s}' nohead".format(num,x1,y1,x2,y2,c)
                print(flecha, file=aristas)
                num += 1              
            pie(self.destino, aristas)


