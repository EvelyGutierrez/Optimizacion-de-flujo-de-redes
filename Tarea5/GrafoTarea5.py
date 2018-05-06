from random import random, uniform, randint
from math import sqrt, ceil, floor

def cabecera(aristas, k, eps=False):
    if eps:
        print("set term postscript color eps", file = aristas)
        print("set output 'GrafoGrid.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'GrafoGrid.png'", file = aristas)
    #print("set xrange [-0.1:1]", file = aristas)
    #print("set yrange [-0.1:1]", file = aristas)
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
                  
            print("nodos")
            print(self.nodos)
            

                                    
        

    def Grafica(self, plot, k): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, 'w') as puntos:
            
            cabecera(puntos, k)
                
            num = 1
            for (v, w, p) in self.aristas:
             
                (x1, y1) = self.nodos[v]
                (x2, y2) = self.nodos[w]                
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 3 lw {:f} nohead".format(num,x1,y1,x2,y2,p)
                
                print(flecha, file=puntos)
                num += 1

            pie(self.destino, puntos)              
                
            
                
    def GraficaNodos(self, plot, k):
        with open(plot, 'w') as puntos:
             cabecera(puntos, k)
             
             puntoss = "plot 'GraficaNodos.txt' with points pt 5"
             print(puntoss, file=puntos)
             

    def getManhattan(self, a,b):
        (x1, y1) = self.nodos[a]
        (x2, y2) = self.nodos[b]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        md = dx + dy
        
        return(md)




    def manhattan(self, k, l, p):

        #conecciones l
        for i in self.nodos:
            for j in self.nodos:
                if (self.getManhattan(i,j) <= l):
                    
                    self.aristas.append((i, j, 1))
                    self.aristas.append((j, i, 1))
                    
                elif (random() < p) :
                    
                   self.aristas.append((i, j, 3))
        

        print('Aristas ')
        print(len(self.aristas))
        print(self.aristas)


    def quitar_nodo(self, u):
        #vecindad = self.vecinos[u].copy()
        #for i in vecindad:
           # print("quité arista con",i)
           # self.quitar_arista(u,i)
        #for n in self.nodos:
            #if u in self.vecinos[n]:
                #print("uy quité arista con",n)
                #self.quitar_arista(n,u)
        self.nodos.remove(u)
        
G1 = Grafo()
G1.puntos("GraficaNodos.txt", 5)
G1.GraficaNodos("NodosGrid.plot", 5)
#G1.quitar_nodo(3)
G1.manhattan(k = 5, l = 1, p = 0.002)
G1.Grafica("GrafoGrid.plot", 5)
