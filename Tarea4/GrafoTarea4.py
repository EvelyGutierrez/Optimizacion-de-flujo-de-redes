print("Pruebas con Aloritmos FloydWarshall y FordFulkerson")
from random import random, choice
from sys import stdout
import time
import math

colores = ["black", "blue", "pink", "orange", "red"]
pesos = [1,2,3]

def cabecera(aristas, eps=False):
    if eps:
        print("set term postscript color eps", file = aristas)
        print("set output 'circulo12.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'circulo12.png'", file = aristas)
    #print("set xrange [-0.1:1]", file = aristas)
    #print("set yrange [-0.1:1]", file = aristas)
    print('set size square', file = aristas) 
    print('set key off', file = aristas)

def pie(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 5  ps 1".format(destino), file = aristas)

class Grafo:
    
    def __init__(self):
        self.n = None # se crean las variables pero aun no se inicializan
        self.x = dict()
        self.y = dict()
        self.E = []
        self.nodos = set()
        self.destino = None
        self.vecinos = dict()
        self.vecinos2 = dict()
        self.posicion = dict()
        self.tamano = dict()
        self.i = None
        self.aristas = dict()
        self.d = None
        self.sumatoria = None
        

    def creaNodos(self, orden): # creando los nodos
        self.n = orden        
        for nodo in range(self.n):
            self.x[nodo] = random()
            self.y[nodo] = random() 

    def imprimir(self, dest): # guardando los pares X y Y en un archivo
        self.destino = dest
        with open(self.destino , "w") as archivo:
            for nodo in range(self.n):
               print(self.x[nodo], self.y[nodo], file=archivo)
        print(self.destino)


    def factorial(self, *n):
        for x in n:
            fac = 1
            for y in range(1,x + 1):
                fac = fac * y
                
        return fac

    def ConectaAristas(self, v, u):
        peso = choice(pesos)
        color = "red"
               
        if not v in self.nodos:
            self.agrega(v)
        if not u in self.nodos:
            self.agrega(u)
        
        self.E.append((self.i, v, u, peso, color))      
        self.vecinos[u].add((int(v), peso))
        self.vecinos2[u].add(int(v))
        self.vecinos[v].add((int(u), peso))
        self.vecinos2[v].add(int(u))
            
    def agrega(self, v, posicion = (0,0)):
        self.nodos.add(v)
        
        self.posicion[v] = posicion
        if not v in self.vecinos:
            self.vecinos[v] = set()
            self.vecinos2[v] = set()

    def GuardaCirculo(self, dest, k, N, prob, r, xo, yo): #Para crear vertices que formen un circulo y guardarlos en un .txt
        self.destino = dest
        self.i = 1
        size = random()
        with open(self.destino , "w") as circulo:
            for n in range(N):
                xn = xo + r *(math.cos(2*math.pi * (n/N)))
                yn = yo + r *(math.sin(2*math.pi * (n/N)))
                print(xn, yn, file = circulo)
                self.x[n] = xn
                self.y[n] = yn
                self.agrega(size, (xn, yn))                        
                           
            for a in range(N):
                for j in range(k):
                    
                    jj = (a+j+1)%n            
                    self.ConectaAristas(str(a),str(jj))
                    self.i += 1                  

            for i in range(n-1):
                for j in range(n-2*k-1):
                    jj = (i+j+k+1)%n
                    if random() < prob:   
                        self.ConectaAristas(str(a),str(jj))
                        
        return self.E

    
    def PlotCirculo(self, plot, circulo): #Para plotear un circulo en gnuplot 
        with open(plot, "w") as circulo:
            cabecera(circulo)                        
            circulos = "plot 'circulo.txt' with points pt 5"
            print(circulos, file=circulo)
            
    def Grafica(self, plot): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            
            for (num, v, w, p, c) in self.E:
                x1 = self.x[int(v)]
                x2 = self.x[int(w)]
                y1 = self.y[int(v)]
                y2 = self.y[int(w)]                 
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 2 lw {:f} lc rgb '{:s}' nohead".format(num,x1,y1,x2,y2,p,c)
                print(flecha, file=aristas)
                
                                             
            pie(self.destino, aristas)
        
    def FloydWarshall(self):
        d = {}
        for nod in range(self.n - 1):
            d[(nod,nod)] = 0 # distancia reflexiva es cero
            for (vecino,peso) in self.vecinos[str(nod)]: # para vecinos, la distancia es el peso               
                d[(nod,vecino)] = peso
        for intermedio in self.vecinos:
            for desde in self.vecinos:
                for hasta in self.vecinos:
                    di = None
                    if (desde,intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio,hasta) in d:
                        ih = d[(intermedio,hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual

           
        return d


    def avgdist(self): #Promedio de las distancias
        self.d = self.FloydWarshall()
        self.sumatoria = sum(self.d.values())/ len(self.d)
        return self.sumatoria

  
    def clustcoef2(self):
        
        g = len(self.vecinos2) - 1
        valor = 0
        for v in range(1, g):
            m = 0
            for u in self.vecinos2[str(v)]:
                for w in self.vecinos2[str(v)]:
                    if u in self.vecinos2[str(w)]:
                        m+= 1
            n = len(self.vecinos2[str(v)])
            if n > 1: 
                valor += m/(n*(n-1))                
        return(valor/g)
    
    def ver(self):
      
        a = self.vecinos
        return a

    def cota(self, n, k, r): #Cota superior no me funciona bien
        pi = 3.14
        circulo = 2*(pi)*r*r
        
        superior = circulo/(len(self.d)/k)-n
        
        if superior < self.sumatoria/n:
            cota = (self.sumatoria/n)/superior              
            return cota   
        
    def PlotDiagrama1(self, plot, diagrama): #Diagrama de tiempos  
        with open(plot, "w") as diagrama:
            print("set terminal png truecolor", file = diagrama)
            print("set output 'Diagrama1.png'", file = diagrama)
            print("set key off", file = diagrama)

            print("set title 'Diagramas de tiempos logaritmicos'", file = diagrama)
            print("set xlabel 'Potencias de 2 nodos por grafo'", file = diagrama)
            print("set ylabel 'Logaritmo de tiempo de procesamiento'", file = diagrama)
            #set logscale y
            print("set style fill solid 0.25 border -1", file = diagrama)
            print("set style boxplot outliers pointtype 7", file = diagrama)
            print("set style data boxplot", file = diagrama)
            #f(x) = 150 * exp(x) - 12

            diagrama1 = "plot 'TiempoFWTarea4.txt' using (-8):(log($3)):(0.5):1"                       
            
            print(diagrama1, file=diagrama)

    def PlotDiagrama2(self, plot, diagrama): #Diagrama Distancia promedio contra densidad
        with open(plot, "w") as diagrama:
            print("set terminal png truecolor", file = diagrama)
            print("set output 'Diagrama2.png'", file = diagrama)
            print("set key off", file = diagrama)

            print("set title 'Diagramas de tiempos logaritmicos'", file = diagrama)
            print("set xlabel 'Potencias de 2 nodos por grafo'", file = diagrama)
            print("set ylabel 'Logaritmo de tiempo de procesamiento'", file = diagrama)
            #set logscale y
            print("set style fill solid 0.25 border -1", file = diagrama)
            print("set style boxplot outliers pointtype 7", file = diagrama)
            print("set style data boxplot", file = diagrama)
            #f(x) = 150 * exp(x) - 12

            diagrama1 = "plot 'ProbTarea4.txt' using (-8):(log($3)):(0.5):1"                       
            
            print(diagrama1, file=diagrama)
