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
        for nodo in range(self.n - 1):
            for otro in range(nodo + 1, self.n):           
                if random() < prob:                    
                    peso = choice(pesos)
                    color = choice(colores)
                    if peso > 0:
                        self.E.append((nodo, otro, peso, color))
                        if not nodo in self.vecinos: # vecindad de nodo
                            self.vecinos[nodo] = set()
                        if not otro in self.vecinos: # vecindad de otro
                            self.vecinos[otro] = set()    
                        self.vecinos[nodo].add((otro, peso))
                        self.vecinos[otro].add((nodo, peso))
                        print(peso)
                        
        print(len(self.E))
        print(self.vecinos)
        

    def grafica(self, plot): # imprimiendo el grafo con aristas
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            num = 1
            for (v, w, p, c) in self.E:                
                x1 = self.x[v]
                x2 = self.x[w]
                y1 = self.y[v]
                y2 = self.y[w]              
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 5 lw {:f} lc rgb '{:s}' head".format(num,x1,y1,x2,y2,p,c)
                print(flecha, file=aristas)
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
            for (w, v, p, c) in self.E:
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



    def GraficoCajaBigote(self):
        import matplotlib.pyplot as plt 
        
        # Ejemplo de grafico de cajas en python

        datos_1 = 1
        datos_2 = 10
        datos_3 = 20
        datos_4 = 5

        datos_graf = [datos_1, datos_2, datos_3, datos_4]

        # Creando el objeto figura
        fig = plt.figure(1, figsize=(9, 6))

        # Creando el subgrafico
        ax = fig.add_subplot(111)

        # creando el grafico de cajas
        bp = ax.boxplot(datos_graf)

        # visualizar mas facile los atípicos
        for flier in bp['fliers']:
            flier.set(marker='o', color='red', alpha=0.5)
        # los puntos aislados son valores atípicos

    
        #plt.ion()  # Nos ponemos en modo interactivo
        #alt_esp = np.random.randn(100)+165 + np.random.randn(100) * 10  # Creamos unos valores para la altura de 100 españolas
        #alt_ale = np.random.randn(100)+172 + np.random.randn(100) * 12  # Creamos unos valores para la altura de 100 alemanas
        #alt_tai = np.random.randn(100)+159 + np.random.randn(100) * 9   # Creamos unos valores para la altura de 100 tailandesas
        #plt.boxplot([alt_esp, alt_ale, alt_tai], sym = 'ko', whis = 1.5)  # El valor por defecto para los bigotes es 1.5*IQR pero lo escribimos explícitamente
        #plt.xticks([1,2,3], ['Esp', 'Ale', 'Tai'], size = 'small', color = 'k')  # Colocamos las etiquetas para cada distribución
        #plt.ylabel(u'Altura (cm)')



    def GraficaErrorB(self):
        # Definir tipo de salida para gnuplot
        print("set term postscript eps color solid rounded blacktext “Helvetica” 20 enhanced")
        # Nombre de los ejes
        print("set xlabel “x”")
        print("set ylabel “y”")

        # Establecer rejilla
        print("set grid")

        # Establecer rango de los datos para el eje x e y
        print("set yrange [0:40]")
        print("set xrange [0:40]")

        # Sitúa la leyenda abajo a la derecha
        print("set key right bottom")

        # Nombre del fichero en el que guardaremos la gráfica
        print("set output ‘ejemplo_barras_errores.eps’")

        # Función de ajuste para los datos
        f = 20 + 10

        # Ajuste de los datos según la función f
        print("fit f(x) ‘datos.txt’ u 1:2 via a, b")

        # Pintar la función, por un lado se pinta el ajuste y por otro los datos
        print("plot {:f} lc rgb “blue”, \
        ‘datos.txt’ u 1:2:3:4 with xyerrorbars lc rgb “red” notitle, \
        ‘datos.txt’ u 1:2 with points pointtype 7 lc rgb “white” notitle, \
        ‘datos.txt’ u 1:2 with points pointtype 6 lc rgb “red” title ‘x:y’".format(f))

    
