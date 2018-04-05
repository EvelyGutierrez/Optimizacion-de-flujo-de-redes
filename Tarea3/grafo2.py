print("hola")
from random import random, choice
from sys import stdout

colores = ["black", "blue", "pink", "orange", "red"]
pesos = [1,2,3,4,5,6,7,8,9,10]

def cabecera(aristas, eps=True):
    if eps:
        print("set term postscript color eps", file = aristas)
        print("set output 'tarea3.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'tarea3.png'", file = aristas)
    print("set xrange [-0.1:1]", file = aristas)
    print("set yrange [-0.1:1]", file = aristas)
    print('set size square', file = aristas) 
    print('set key off', file = aristas)

def pie(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 7  ps 1".format(destino), file = aristas)

class Grafo:
    
    def __init__(self):
        self.n = None # se crean las variables pero aun no se inicializan
        self.x = dict()
        self.y = dict()
        self.E = []
        self.destino = None
        self.vecinos = dict()
        self.i = None
        

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

    def conecta(self, prob):
        self.i = 1
        for nodo in range(self.n - 1):
            for otro in range(nodo + 1, self.n):           
                if random() < prob:                    
                    peso = choice(pesos)
                    color = choice(colores)                    
                    if peso > 0:
                        self.E.append((self.i, nodo, otro, peso, color))
                        self.i += 1
                        if not nodo in self.vecinos: # vecindad de nodo
                            self.vecinos[nodo] = set()
                        if not otro in self.vecinos: # vecindad de otro
                            self.vecinos[otro] = set()    
                        self.vecinos[nodo].add((otro, peso))
                        self.vecinos[otro].add((nodo, peso))
        return len(self.E)                                   
        #print(self.E)
        #print(self.vecinos)
        

    def grafica(self, plot): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            num = 1
            for (num,v, w, p, c) in self.E:                
                x1 = self.x[v]
                x2 = self.x[w]
                y1 = self.y[v]
                y2 = self.y[w]              
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 5 lw {:f} lc rgb '{:s}' nohead".format(num,x1,y1,x2,y2,p,c)
                #flecha = "set arrow " + srt(num) + "from " + str(x1) + "," + str(y1) + " to " + str(x2) + "," + str(y2) + " lt 5 lw {:f} lc rgb '{:s}' head".format(num,p,c)
                #print(flecha, file=aristas)
                num += 1              
            pie(self.destino, aristas)

    def FloydWarshall(self): 
        d = {}
        for nodo in range(self.n - 1):
            d[(nodo, nodo)] = 0 # distancia reflexiva es cero
            for (vecino, peso) in self.vecinos[nodo]: # para vecinos, la distancia es el peso
                d[(nodo, vecino)] = peso
        for intermedio in self.vecinos:
            for desde in self.vecinos:
                for hasta in self.vecinos:
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual
        return d


# u son mis vecinos
# v son mis nodos
# w 


    def camino(self, s, t, f): # construcciÃ³n de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (i,w, v, p, c) in self.E:
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
        print(maximo)


