print("hola")
from random import random
nodos = []
n = 15

with open ("nodos.dat" , "w") as nodo:
    for nod in range(n):
        x = random()*10
        y = random()*10
        nodos.append((x,y))
        print(x,y,file=nodo)


with open("grafo.plt" , "w") as aristas:
    print("set xrange [-10.0:10.0]", file = aristas)
    print("set yrange [-10.0:10.0]", file = aristas)
    num = 1
    for (x1,y1) in nodos:
        for (x2,y2) in nodos:           
            if random() < 0.1:
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 2 lt 5 lc rgb 'red' nohead".format(num,x1,y1,x2,y2),file= aristas)
                num += 1
                if random() > 0.5:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 4 lt 5 lc rgb 'blue' nohead".format(num,x1,y1,x2,y2),file= aristas)
                    num += 1  

    print('set size square', file = aristas) 
    print('set key off', file = aristas)
    print('set title "Lineas del Metro"', file = aristas)
    print('set xlabel "Linea 1"', file = aristas)
    print('set ylabel "Linea 2"', file = aristas)
    print('set xrange[0:10]', file = aristas)
    print('set yrange[0:10]', file = aristas)
    print("plot 'nodos.dat' using 1:2 with points pt 5", file = aristas)   

print("termino")

