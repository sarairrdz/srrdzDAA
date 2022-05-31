"""
Proyecto 1 - Biblioteca de generación y manejo de grafos
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

#### Ejecución de Generación de Grafos (30,100 y 500 nodos) ###

from graph import Graph
from algorithms import *


#Modelo de malla
g1 = graphGrid(5,6)
saveGraph_GV(g1)

g2 = graphGrid(10,10)
saveGraph_GV(g2)

g3 = graphGrid(50,10)
saveGraph_GV(g3)


# Modelo Erdos Renyi 
g4 = graph_Erdos_Renyi(30,50)
saveGraph_GV(g4)

g5 = graph_Erdos_Renyi(100,400)
saveGraph_GV(g5)

g6 = graph_Erdos_Renyi(500,2000)
saveGraph_GV(g6)


#Modelo de Gilbert
g7 = graph_Gilbert(30,0.5)
saveGraph_GV(g7)

g8 = graph_Gilbert(100,0.3)
saveGraph_GV(g8)

g9 = graph_Gilbert(500,0.7)
saveGraph_GV(g9)


#Modelo Geográfico 
g10 = graph_Geographic(30,0.4)
saveGraph_GV(g10)

g11 = graph_Geographic(100,0.5)
saveGraph_GV(g11)

g12 = graph_Geographic(500,0.4)
saveGraph_GV(g12)

#Modelo Barabasi Albert
g13 =  graph_BarabasiAlbert(30,5)
saveGraph_GV(g13)

g14 =  graph_BarabasiAlbert(100,5)
saveGraph_GV(g14)

g15 =  graph_BarabasiAlbert(500,5)
saveGraph_GV(g15)

#Modelo Dorogovtsev Mendes
g16 = graph_DorogovtsevMendes(30)
saveGraph_GV(g16)

g17 = graph_DorogovtsevMendes(100)
saveGraph_GV(g17)

g18 = graph_DorogovtsevMendes(500)
saveGraph_GV(g18)

