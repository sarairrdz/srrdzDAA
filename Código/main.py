"""
Proyecto 2 - Algoritmos BSF y DFS
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

#### Ejecución de Generación de Grafos (30,100 y 500 nodos) ###

from graph import Graph
from algorithms import *


# --- Modelo de malla ---
#30 Nodos
g1 = graphGrid(5,6)
saveGraph_GV(g1)
g1_BFS,L=g1.BFS(0)
saveGraph_GV(g1_BFS)
g1_DFSR=g1.DFS_R(0)
saveGraph_GV(g1_DFSR)
g1_DFSI=g1.DFS_I(0)
saveGraph_GV(g1_DFSI)

#100 Nodos - Malla
g2 = graphGrid(10,10)
saveGraph_GV(g2)
g2_BFS,L=g2.BFS(0)
saveGraph_GV(g2_BFS)
g2_DFSR=g2.DFS_R(0)
saveGraph_GV(g2_DFSR)
g2_DFSI=g2.DFS_I(0)
saveGraph_GV(g2_DFSI)

#500 Nodos - Malla
g3 = graphGrid(50,10)
saveGraph_GV(g3)
g3_BFS,L=g3.BFS(0)
saveGraph_GV(g3_BFS)
g3_DFSR=g3.DFS_R(0)
saveGraph_GV(g3_DFSR)
g3_DFSI=g3.DFS_I(0)
saveGraph_GV(g3_DFSI)


# Modelo Erdos Renyi 
#30 Nodos
g4 = graph_Erdos_Renyi(30,50)
saveGraph_GV(g4)
g4_BFS,L=g4.BFS(0)
saveGraph_GV(g4_BFS)
g4_DFSR=g4.DFS_R(0)
saveGraph_GV(g4_DFSR)
g4_DFSI=g4.DFS_I(0)
saveGraph_GV(g4_DFSI)

#100 Nodos - Erdos Renyi
g5 = graph_Erdos_Renyi(100,400)
saveGraph_GV(g5)
g5_BFS,L=g5.BFS(0)
saveGraph_GV(g5_BFS)
g5_DFSR=g5.DFS_R(0)
saveGraph_GV(g5_DFSR)
g5_DFSI=g5.DFS_I(0)
saveGraph_GV(g5_DFSI)

#500 Nodos - Erdos Renyi
g6 = graph_Erdos_Renyi(500,2000)
saveGraph_GV(g6)
g6_BFS,L=g6.BFS(0)
saveGraph_GV(g6_BFS)
g6_DFSR=g6.DFS_R(0)
saveGraph_GV(g6_DFSR)
g6_DFSI=g6.DFS_I(0)
saveGraph_GV(g6_DFSI)

#Modelo de Gilbert
#30 Nodos
g7 = graph_Gilbert(30,0.5)
saveGraph_GV(g7)
g7_BFS,L=g7.BFS(0)
saveGraph_GV(g7_BFS)
g7_DFSR=g7.DFS_R(0)
saveGraph_GV(g7_DFSR)
g7_DFSI=g7.DFS_I(0)
saveGraph_GV(g7_DFSI)


#100 Nodos - Gilbert
g8 = graph_Gilbert(100,0.3)
saveGraph_GV(g8)
g8_BFS,L=g8.BFS(0)
saveGraph_GV(g8_BFS)
g8_DFSR=g8.DFS_R(0)
saveGraph_GV(g8_DFSR)
g8_DFSI=g8.DFS_I(0)
saveGraph_GV(g8_DFSI)

#500 Nodos - Gilbert
g9 = graph_Gilbert(500,0.7)
saveGraph_GV(g9)
g9_BFS,L=g9.BFS(0)
saveGraph_GV(g9_BFS)
g9_DFSR=g9.DFS_R(0)
saveGraph_GV(g9_DFSR)
g9_DFSI=g9.DFS_I(0)
saveGraph_GV(g9_DFSI)


#Modelo Geográfico 
#30 Nodos
g10 = graph_Geographic(30,0.4)
saveGraph_GV(g10)
g10_BFS,L=g10.BFS(0)
saveGraph_GV(g10_BFS)
g10_DFSR=g10.DFS_R(0)
saveGraph_GV(g10_DFSR)
g10_DFSI=g10.DFS_I(0)
saveGraph_GV(g10_DFSI)

#100 Nodos - Geográfico
g11 = graph_Geographic(100,0.5)
saveGraph_GV(g11)
g11_BFS,L=g11.BFS(0)
saveGraph_GV(g11_BFS)
g11_DFSR=g11.DFS_R(0)
saveGraph_GV(g11_DFSR)
g11_DFSI=g11.DFS_I(0)
saveGraph_GV(g11_DFSI)

#500 Nodos - Geográfico
g12 = graph_Geographic(500,0.4)
saveGraph_GV(g12)
g12_BFS,L=g12.BFS(0)
saveGraph_GV(g12_BFS)
g12_DFSR=g12.DFS_R(0)
saveGraph_GV(g12_DFSR)
g12_DFSI=g12.DFS_I(0)
saveGraph_GV(g12_DFSI)

#Modelo Barabasi Albert
#30 Nodos
g13 =  graph_BarabasiAlbert(30,5)
saveGraph_GV(g13)
g13_BFS,L=g13.BFS(0)
saveGraph_GV(g13_BFS)
g13_DFSR=g13.DFS_R(0)
saveGraph_GV(g13_DFSR)
g13_DFSI=g13.DFS_I(0)
saveGraph_GV(g13_DFSI)

#100 Nodos - Barabasi Albert
g14 =  graph_BarabasiAlbert(100,5)
saveGraph_GV(g14)
g14_BFS,L=g14.BFS(0)
saveGraph_GV(g14_BFS)
g14_DFSR=g14.DFS_R(0)
saveGraph_GV(g14_DFSR)
g14_DFSI=g14.DFS_I(0)
saveGraph_GV(g14_DFSI)

#500 Nodos - Barabasi Albert
g15 =  graph_BarabasiAlbert(500,5)
saveGraph_GV(g15)
g15_BFS,L=g15.BFS(0)
saveGraph_GV(g15_BFS)
g15_DFSR=g15.DFS_R(0)
saveGraph_GV(g15_DFSR)
g15_DFSI=g15.DFS_I(0)
saveGraph_GV(g15_DFSI)

#Modelo Dorogovtsev Mendes
#30 Nodos
g16 = graph_DorogovtsevMendes(30)
saveGraph_GV(g16)
g16_BFS,L=g16.BFS(1)
saveGraph_GV(g16_BFS)
g16_DFSR=g16.DFS_R(1)
saveGraph_GV(g16_DFSR)
g16_DFSI=g16.DFS_I(1)
saveGraph_GV(g16_DFSI)

#100 Nodos - Dorogovtsev Mendes
g17 = graph_DorogovtsevMendes(100)
saveGraph_GV(g17)
g17_BFS,L=g17.BFS(1)
saveGraph_GV(g17_BFS)
g17_DFSR=g17.DFS_R(1)
saveGraph_GV(g17_DFSR)
g17_DFSI=g17.DFS_I(1)
saveGraph_GV(g17_DFSI)

#500 Nodos - Dorogovtsev Mendes
g18 = graph_DorogovtsevMendes(500)
saveGraph_GV(g18)
g18_BFS,L=g18.BFS(1)
saveGraph_GV(g18_BFS)
g18_DFSR=g18.DFS_R(1)
saveGraph_GV(g18_DFSR)
g18_DFSI=g18.DFS_I(1)
saveGraph_GV(g18_DFSI)
