"""
Proyecto 4 - Algoritmos de Kruskal y Prim
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

#### Ejecución de Generación de Grafos + Algoritmos Kruskall y Prim###

from graph import Graph
from algorithms import *



#Modelo de malla
#30 Nodos
g1 = graphGrid(5,6)
print("Modelo Generador: MALLA \n# Nodos: 30 \n")
#Kruskall D
g1_KD=g1.KruskalD()
print(g1_KD.getType())
print(f"Valor MST: {g1_KD.mst} \n")
#Kruskall I
g1_KI=g1.KruskalI()
print(g1_KI.getType())
print(f"Valor MST: {g1_KI.mst} \n")
#Prim
g1_P=g1.Prim()
print(g1_P.getType())
print(f"Valor MST: {g1_P.mst}\n")
#save
saveGraph_GV(g1)
saveGraph_GV(g1_KD)
saveGraph_GV(g1_KI)
saveGraph_GV(g1_P)


#Modelo de malla
#300 Nodos
g2 = graphGrid(20,15)
print("Modelo Generador: MALLA \n# Nodos: 300 \n")
#Kruskall D
g2_KD=g2.KruskalD()
print(g2_KD.getType())
print(f"Valor MST: {g2_KD.mst} \n")
#Kruskall I
g2_KI=g2.KruskalI()
print(g2_KI.getType())
print(f"Valor MST: {g2_KI.mst} \n")
#Prim
g2_P=g2.Prim()
print(g2_P.getType())
print(f"Valor MST: {g2_P.mst}\n")
#save
saveGraph_GV(g2)
saveGraph_GV(g2_KD)
saveGraph_GV(g2_KI)
saveGraph_GV(g2_P)


# Modelo Erdos Renyi 
#30 Nodos
g4 = graph_Erdos_Renyi(30,50)
print("Modelo Generador: Erdos-Renyi \n# Nodos: 30 \n")
#Kruskall D
g4_KD=g4.KruskalD()
print(g4_KD.getType())
print(f"Valor MST: {g4_KD.mst} \n")
#Kruskall I
g4_KI=g4.KruskalI()
print(g4_KI.getType())
print(f"Valor MST: {g4_KI.mst} \n")
#Prim
g4_P=g4.Prim()
print(g4_P.getType())
print(f"Valor MST: {g4_P.mst}\n")
#save
saveGraph_GV(g4)
saveGraph_GV(g4_KD)
saveGraph_GV(g4_KI)
saveGraph_GV(g4_P)

#100 Nodos
g5 = graph_Erdos_Renyi(100,500)
print("Modelo Generador: Erdos-Renyi \n# Nodos: 100 \n")
#Kruskall D
g5_KD=g5.KruskalD()
print(g5_KD.getType())
print(f"Valor MST: {g5_KD.mst} \n")
#Kruskall I
g5_KI=g5.KruskalI()
print(g5_KI.getType())
print(f"Valor MST: {g5_KI.mst} \n")
#Prim
g5_P=g5.Prim()
print(g5_P.getType())
print(f"Valor MST: {g5_P.mst}\n")
#save
saveGraph_GV(g5)
saveGraph_GV(g5_KD)
saveGraph_GV(g5_KI)
saveGraph_GV(g5_P)

#Modelo de Gilbert
#30 Nodos
g7 = graph_Gilbert(30,0.5)
print("Modelo Generador: Gilbert \n# Nodos: 30 \n")
#Kruskall D
g7_KD=g7.KruskalD()
print(g7_KD.getType())
print(f"Valor MST: {g7_KD.mst} \n")
#Kruskall I
g7_KI=g7.KruskalI()
print(g7_KI.getType())
print(f"Valor MST: {g7_KI.mst} \n")
#Prim
g7_P=g7.Prim()
print(g7_P.getType())
print(f"Valor MST: {g7_P.mst}\n")
#save
saveGraph_GV(g7)
saveGraph_GV(g7_KD)
saveGraph_GV(g7_KI)
saveGraph_GV(g7_P)

#300 Nodos
g8 = graph_Gilbert(300,0.5)
print("Modelo Generador: Gilbert \n# Nodos: 300 \n")
#Kruskall D
g8_KD=g8.KruskalD()
print(g8_KD.getType())
print(f"Valor MST: {g8_KD.mst} \n")
#Kruskall I
g8_KI=g8.KruskalI()
print(g8_KI.getType())
print(f"Valor MST: {g8_KI.mst} \n")
#Prim
g8_P=g8.Prim()
print(g8_P.getType())
print(f"Valor MST: {g8_P.mst}\n")
#save
saveGraph_GV(g8)
saveGraph_GV(g8_KD)
saveGraph_GV(g8_KI)
saveGraph_GV(g8_P)


#Modelo Geográfico
# 30 Nodos 
g10 = graph_Geographic(30,0.4)
print("Modelo Generador: Geográfico \n# Nodos: 30 \n")
#Kruskall D
g10_KD=g10.KruskalD()
print(g10_KD.getType())
print(f"Valor MST: {g10_KD.mst} \n")
#Kruskall I
g10_KI=g10.KruskalI()
print(g10_KI.getType())
print(f"Valor MST: {g10_KI.mst} \n")
#Prim
g10_P=g10.Prim()
print(g10_P.getType())
print(f"Valor MST: {g10_P.mst}\n")
#save
saveGraph_GV(g10)
saveGraph_GV(g10_KD)
saveGraph_GV(g10_KI)
saveGraph_GV(g10_P)

#300 Nodos
g11 = graph_Geographic(300,0.5)
print("Modelo Generador: Geográfico \n# Nodos: 300 \n")
#Kruskall D
g11_KD=g11.KruskalD()
print(g11_KD.getType())
print(f"Valor MST: {g11_KD.mst} \n")
#Kruskall I
g11_KI=g11.KruskalI()
print(g11_KI.getType())
print(f"Valor MST: {g11_KI.mst} \n")
#Prim
g11_P=g11.Prim()
print(g11_P.getType())
print(f"Valor MST: {g11_P.mst}\n")
#save
saveGraph_GV(g11)
saveGraph_GV(g11_KD)
saveGraph_GV(g11_KI)
saveGraph_GV(g11_P)


#Modelo Barabasi Albert
#30 Nodos
g13 =  graph_BarabasiAlbert(30,5)
print("Modelo Generador: Barabasi - Albert \n# Nodos: 30 \n")
#Kruskall D
g13_KD=g13.KruskalD()
print(g13_KD.getType())
print(f"Valor MST: {g13_KD.mst} \n")
#Kruskall I
g13_KI=g13.KruskalI()
print(g13_KI.getType())
print(f"Valor MST: {g13_KI.mst} \n")
#Prim
g13_P=g13.Prim()
print(g13_P.getType())
print(f"Valor MST: {g13_P.mst}\n")
#save
saveGraph_GV(g13)
saveGraph_GV(g13_KD)
saveGraph_GV(g13_KI)
saveGraph_GV(g13_P)

#300 Nodos
g14 =  graph_BarabasiAlbert(300,5)
print("Modelo Generador: Barabasi - Albert \n# Nodos: 300 \n")
#Kruskall D
g14_KD=g14.KruskalD()
print(g14_KD.getType())
print(f"Valor MST: {g14_KD.mst} \n")
#Kruskall I
g14_KI=g14.KruskalI()
print(g14_KI.getType())
print(f"Valor MST: {g14_KI.mst} \n")
#Prim
g14_P=g14.Prim()
print(g14_P.getType())
print(f"Valor MST: {g14_P.mst}\n")
#save
saveGraph_GV(g14)
saveGraph_GV(g14_KD)
saveGraph_GV(g14_KI)
saveGraph_GV(g14_P)


#Modelo Dorogovtsev Mendes
#30 Nodos
g16 = graph_DorogovtsevMendes(30)
print("Modelo Generador: Dorogovtsev - Mendes \n# Nodos: 30 \n")
#Kruskall D
g16_KD=g16.KruskalD()
print(g16_KD.getType())
print(f"Valor MST: {g16_KD.mst} \n")
#Kruskall I
g16_KI=g16.KruskalI()
print(g16_KI.getType())
print(f"Valor MST: {g16_KI.mst} \n")
#Prim
g16_P=g16.Prim()
print(g16_P.getType())
print(f"Valor MST: {g16_P.mst}\n")
#save
saveGraph_GV(g16)
saveGraph_GV(g16_KD)
saveGraph_GV(g16_KI)
# saveGraph_GV(g16_P)


#300 Nodos
g17 = graph_DorogovtsevMendes(200)
print("Modelo Generador: Dorogovtsev - Mendes \n# Nodos: 300 \n")
#Kruskall D
g17_KD=g17.KruskalD()
print(g17_KD.getType())
print(f"Valor MST: {g17_KD.mst} \n")
#Kruskall I
g17_KI=g17.KruskalI()
print(g17_KI.getType())
print(f"Valor MST: {g17_KI.mst} \n")
#Prim
g17_P=g17.Prim()
print(g17_P.getType())
print(f"Valor MST: {g17_P.mst}\n")
#save
saveGraph_GV(g17)
saveGraph_GV(g17_KD)
saveGraph_GV(g17_KI)
saveGraph_GV(g17_P)

