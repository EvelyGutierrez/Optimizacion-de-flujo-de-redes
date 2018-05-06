from random import random, uniform, randint, gauss, expovariate
from math import sqrt, ceil, floor, factorial, cos, sin, pi
from datetime import datetime
from time import clock
 

def cabecera(aristas, k, eps=True):
    if eps:
        print("set term postscript color eps", file = aristas)
        print("set output 'GrafoGrid.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'GrafoGrid.png'", file = aristas)
    
    print('set xrange [-1:', k , ']', file = aristas)
    print('set yrange [-1:', k , ']', file = aristas)
    print('set size square', file = aristas) 
    print('set key off', file = aristas)

def pie(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 5  ps 1".format(destino), file = aristas)

class Grafo:

    def __init__(self):
        
        self.x = dict()
        self.y = dict()
        self.nodos = dict()
        self.aristas = []
        self.vecinos = dict()
        self.peso = 1
        self.destino = None
        


    def agregaNodos(self,v,x,y):
        self.nodos[v] = (x,y)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
        with open("GraficaNodos.txt", 'a') as archivo:
            print(x,y,v, file = archivo)

            
    def puntos(self, dest, k):
        self.destino = dest        
        
        with open(self.destino, 'w') as puntos:
            it= 0
            for i in range(k):
                for j in range(k):
                    
                    x = i
                    y = j
                       
                    self.agregaNodos(it,x,y)
                    it += 1
                  
           # print("nodos")
            #print(self.nodos)
            

                                    
        

    def Grafica(self, plot, k): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, 'w') as puntos:
            
            cabecera(puntos, k)
                
            num = 1
            for (v, w, p, c) in self.aristas:
             
                (x1, y1) = self.nodos[v]
                (x2, y2) = self.nodos[w]                
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 3 lw {:f} lc rgb '{:s}' nohead ".format(num,x1,y1,x2,y2,p, c)
                
                print(flecha, file=puntos)
                num += 1

            pie(self.destino, puntos)              
            print(len(self.aristas))    
            
                
    def GraficaNodos(self, plot, k):
        with open(plot, 'w') as puntos:
             cabecera(puntos, k)
             
             puntoss = "plot 'GraficaNodos.txt' with points pt 4"
             print(puntoss, file=puntos)
             

    def getManhattan(self, a,b):
        (x1, y1) = self.nodos[a]
        (x2, y2) = self.nodos[b]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        md = dx + dy
        
        return(md)




    def manhattan(self, k, l, p):
        
        mu = 10
        sigma = 5
        lmbd = 2


        color = 'black'
        cantidad = 0
        peso1 = 0
        peso2 = 0
        #conecciones l
        for i in self.nodos:
            for j in self.nodos:
                if (self.getManhattan(i,j) <= l):
                    peso1 = gauss(mu,sigma)
                    peso1 = abs(int(peso1))+1
                    
                    self.aristas.append((i, j, peso1, color))
                    self.aristas.append((j, i, peso1, color))
                    
                    self.vecinos[i].add(j)
                    
                    self.vecinos[j].add(i)
                    
                    
                elif (random() < p) :
                   color2 = 'blue'
                   cantidad += 1
                   peso2 = expovariate(lmbd)*mu/4
                   peso2 = abs(int(peso2))+1
                   
                   
                   self.aristas.append((i, j, peso2, color2))
                   self.vecinos[i].add(j) 

        #print('Cantidad de aristas aleatorias ')
        
        #print(cantidad)
        print("Aristas******")
        print(len(self.aristas))
        #print(self.vecinos)
        

    def camino(self, s, t, f): # construcciÃ³n de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (w, v, p, c) in self.aristas:
                if w == u and v not in cola and v not in usados:
                    actual = f.get((u, v), 0)
                    dif = p - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if t in usados:
            return camino
        else: # no se alcanzÃ³
            return None
 
 
 
    def FordFulkerson(self, s, t): # algoritmo de Ford y Fulkerson
        if s == t:
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(s, t, f)
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = t
            while u in aum:
                v = aum[u][0]
                actual = f.get((v, u), 0) # cero si no hay
                inverso = f.get((u, v), 0)
                f[(v, u)] = actual + incr
                f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        
        return maximo



    def EliminaArista(self, u,v):

        f = self.aristas[u]
        g = self.aristas[v]
        #print(f)
        print(g)
        self.aristas.remove(f)
        self.aristas.remove(g)
        #print(self.vecinos)
        self.vecinos[u].remove(v)
        if not f:        
            self.vecinos[v].remove(u)

        print(len(self.aristas))    

    def EliminaNodo(self, u):
        vecindad = self.vecinos[u].copy()
        for i in vecindad:
            print("quité arista con",i)
            self.EliminaArista(u,i)
        for n in self.nodos:
            if u in self.vecinos[n]:
                print("uy quité arista con",n)
                self.EliminaArista(n,u)
        
        h = self.nodos.pop(u)
        print(self.nodos)
        print(len(self.aristas))
        
        
    def PlotDiagrama1(self, plot, diagrama): #Diagrama de tiempos  
        with open(plot, "w") as diagrama:
            print("set term postscript color eps", file = diagrama)
            print("set output 'DiaLVSFlujo.eps'", file = diagrama)
            print("set key off", file = diagrama)

           
            print("set xlabel 'Flujo Máximo'", file = diagrama)
            print("set ylabel 'Valores de Distancia L'", file = diagrama)
            #set logscale y
            print("set style fill solid 0.25 border -1", file = diagrama)
            print("set style line 1 lt 1 linecolor rgb 'blue' lw 2 pt 1", file = diagrama)
            print("set style data boxplot", file = diagrama)
            #f(x) = 150 * exp(x) - 12

            diagrama1 = "plot 'TiempoLVSFM.txt' using 1:2 ls 1 title 'Distancias VS Flujo Máximo' with lines "                       
            
            print(diagrama1, file=diagrama)


    def PlotDiagrama2(self, plot, diagrama): #Diagrama de tiempos  
        with open(plot, "w") as diagrama:
            print("set term postscript color eps", file = diagrama)
            print("set output 'DiaArisVSFlujo.eps'", file = diagrama)
            print("set key off", file = diagrama)

           
            print("set xlabel 'Flujo Máximo'", file = diagrama)
            print("set ylabel 'Aristas Eliminadas'", file = diagrama)
            #set logscale y
            print("set style fill solid 0.25 border -1", file = diagrama)
            print("set style boxplot outliers pointtype 7", file = diagrama)
            print("set style data boxplot", file = diagrama)
            #f(x) = 150 * exp(x) - 12

            diagrama2 = "plot 'AristasVSFlujo.txt' using 1:2 "                      
            
            print(diagrama2, file=diagrama)            




k = 20
n = k * k
l = 2
x = 0
flujoMaximo = []
fo = 10
cantAristas = 0
with open("AristasVSFlujo.txt", "a") as f:
    with open("TiempoEjecucion.txt", "a") as d:
        for t in range(0, 1):
            print("Iteracion ------------------------------------------ " + str(l))
            G1 = Grafo()
            G1.puntos("GraficaNodos.txt", k)
            G1.GraficaNodos("NodosGrid.plot", k)
            #G1.quitar_nodo(3)
            
            TiempoInicial = clock() # Tiempo Inicial 
            G1.manhattan(k, l, p = 0.008)
            #FlujoMaximo = G1.FordFulkerson(0, n - 1)
            #print("Flujo Original")
            #print(FlujoMaximo)
            G1.Grafica("GrafoGrid.plot", k)
            
            FlujoMaximo=0
            for x in range(0, fo):
                print(x)
                cantAristas = cantAristas + 2
                G1.EliminaArista(x, x+1)
                #G1.EliminaNodo(5)
                FlujoMaximo = G1.FordFulkerson(0, n - 1)
                print('Flujo maximo eliminando')
                print(FlujoMaximo)
                flujoMaximo.append( FlujoMaximo)
                f.write('{}  {}  {} \n'.format(cantAristas , fo, '%.2f' % FlujoMaximo))
            
                
            
            
            

            TiempoFinal = clock() - TiempoInicial
            d.write('{}  {} \n'.format('%.2f' % TiempoFinal, '%.2f' % x))
            print("Tiempo de ejecucion: ")
            print(TiempoFinal)      
            
            l += 1

G1.PlotDiagrama2("DiaAriVSFlujo.plot", "AristasVSFlujo")



