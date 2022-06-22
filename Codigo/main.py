"""
Proyecto 3 - Algoritmo de Dijkstra
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

#### Ejecución de Generación de Grafos + Algoritmo Dijkstra###

from graph import Graph
from algorithms import *

#Modelo de malla
#40 Nodos
g1 = graphGrid(5,8) 
saveGraph_GV(g1)
g1_D = g1.Dijkstra(0)
print(g1_D.getType())
saveGraph_GV(g1_D)
#400 Nodos
g2 = graphGrid(20,20)
saveGraph_GV(g2)
g2_D = g2.Dijkstra(0)
print(g2_D.getType())
saveGraph_GV(g2_D)


# Modelo Erdos Renyi 
#40 Nodos
g4 = graph_Erdos_Renyi(40,100)
saveGraph_GV(g4)
g4_D = g4.Dijkstra(0)
print(g4_D.getType())
saveGraph_GV(g4_D)
#400 Nodos
g5 = graph_Erdos_Renyi(400,1000)
saveGraph_GV(g5)
g5_D = g5.Dijkstra(0)
print(g5_D.getType())
saveGraph_GV(g5_D)



#Modelo de Gilbert
#40 Nodos
g7 = graph_Gilbert(40,0.5)
saveGraph_GV(g7)
g7_D = g7.Dijkstra(0)
print(g7_D.getType())
saveGraph_GV(g7_D)
#400 Nodos
g8 = graph_Gilbert(400,0.3)
saveGraph_GV(g8)
g8_D = g8.Dijkstra(0)
print(g8_D.getType())
saveGraph_GV(g8_D)


#Modelo Geográfico 
#40 Nodos
g10 = graph_Geographic(40,0.4)
saveGraph_GV(g10)
g10_D = g10.Dijkstra(0)
print(g10_D.getType())
saveGraph_GV(g10_D)
#400 Nodos
g11 = graph_Geographic(400,0.5)
saveGraph_GV(g11)
g11_D = g11.Dijkstra(0)
print(g11_D.getType())
saveGraph_GV(g11_D)

#Modelo Barabasi Albert
#40 Nodos
g13 =  graph_BarabasiAlbert(40,5)
saveGraph_GV(g13)
g13_D = g13.Dijkstra(0)
print(g13_D.getType())
saveGraph_GV(g13_D)

#400 Nodos
g14 =  graph_BarabasiAlbert(400,5)
saveGraph_GV(g14)
g14_D = g14.Dijkstra(0)
print(g14_D.getType())
saveGraph_GV(g14_D)


#Modelo Dorogovtsev Mendes
#40 Nodos
g16 = graph_DorogovtsevMendes(30)
saveGraph_GV(g16)
g16_D = g16.Dijkstra(1)
print(g16_D.getType())
saveGraph_GV(g16_D)

#400 Nodos
g17 = graph_DorogovtsevMendes(400)
saveGraph_GV(g17)
g17_D = g17.Dijkstra(1)
print(g17_D.getType())
saveGraph_GV(g17_D)