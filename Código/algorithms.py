"""
Proyecto 4 - Algoritmos de Kruskal y Prim
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""
### ALGORITMOS PARA LA GENERACIÓN de GRAFOS ###

from graph import Graph
import random
import numpy as np


#Tipos de grafo
GRID_GRAPH = 0
ERDOS_RENYI_GRAPH = 1
GILBERT_GRAPH = 2
GEOGRAPHIC_GRAPH = 3
BARABASI_ALBERT_GRAPH = 4
DOROGOGOVTSEV_MENDES_GRAPH = 5
BFS_TREE = 6
DFS_R_TREE = 7
DFS_I_TREE = 8
DIJKSTRA_TREE=9
KRUSKALL_D=10
KRUSKALL_I=11
PRIM=12
GENERATOR_NONE=100






def graphGrid(m, n=0, dirigido=False):
    """
    Genera un grafo de malla --  Crear m*n nodos.   --Generate a grid graph  Create m*n nodes.  
    Para el nodo ni,j crear una arista con el nodo ni+1,j y otra con el nodo ni,j+1, para i<m y j<n 
    :param m: número de columnas(m > 1) -- columns
    :param n: número de filas (n > 1) -- rows
    :param dirigido: Booleano de grafo dirigido   -- Directed Graph True/False:
    :return grafo generado -- graph generated 
    """
    # Malla cuadrada si n=0 o si no se pasa n
    if n == 0:
        n = m

    #por lo menos debe ser un cuadrado
    m = max(2,m)
    n = max(2,n)

    # Se crea el grafo

    g = Graph()
    g.type=GRID_GRAPH
    g.generator=GENERATOR_NONE
    
    for i in range(m):
        for j in range(n):
            indiceNodos=i*n+j
            ln=(i + 1) * n + j

            if j < n-1: #Derecha
                g.addEdge(indiceNodos,indiceNodos+1,f"{indiceNodos}->{indiceNodos+1}")
                

            if i < m-1: #Izquierda
                g.addEdge(indiceNodos,ln,f"{indiceNodos}->{ln}")

    print(f"Grafo malla de {m}*{n} ha sido creado")
    return g

def graph_Erdos_Renyi(n,m,dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi -- Generates random graph with the Erdos-Renyi model 
    :param n: número de nodos (> 0)  -- number of nodes
    :param m: número de aristas (>= n-1) -- number of edges
    :param dirigido: el grafo es dirigido  -- directed graph Bool
    :return: grafo generado -- graph generated
    """
    #Crear Grafo
    g = Graph()
    g.type=ERDOS_RENYI_GRAPH
    g.generator=GENERATOR_NONE

    #Crear n nodos
    for i in range(n):
        g.addNode(i)
    
    #Elegir al azar m distintos pares de nodos
    for i in range(m):
        source = random.randint(0,n-1)
        target = random.randint(0,n-1)
        if source!=target:
            #Si los nodos son diferentes se agrega arista
            g.addEdge(source,target,f"{source}->{target}")
    print(f"Grafo {g.getType()} ha sido creado")

    return g


def graph_Gilbert(n,p=0.5,dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert -- Generates random graph with  Gilbert  model 
    :param n: número de nodos (n > 0) -- number of nodes (n > 0)
    :param p: probabilidad de crear una arista (0, 1)  -- probability of forming an edge (0, 1)  
    :param dirigido: el grafo es dirigido -- directed graph Bool
    :return: grafo generado  -- graph generated
    """ 
    #Crear Grafo
    g = Graph()
    g.type=GILBERT_GRAPH
    g.generator=GENERATOR_NONE

    #Crear n nodos
    for i in range(n):
        g.addNode(i)
    
    for i in range(n):
        for j in range(n):
            #Se agregan as aristas dependiendo de la probabilidad deseada p
            if random.random() <= p:
                if j != i:
                    g.addEdge(i,j,f"{i}->{j}")
    print(f"Grafo {g.getType()} ha sido creado")
    return g


def graph_Geographic(n,r=0.5,dirigido=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple --  Generates random graph with simple geographic model 
    :param n: número de nodos (n > 0) -- number of nodes (n > 0)
    :param r: distancia máxima para crear un nodo (0, 1) -- maximum distance to create a node (0, 1)
    :param dirigido: el grafo es dirigido -- directed graph Bool
    :return: grafo generado  -- graph generated
    """

    #Se crea el grafo
    g = Graph()
    g.type=GEOGRAPHIC_GRAPH
    g.generator=GENERATOR_NONE

    #Crear n nodos
    for i in range(n):
        g.addNode(i) #Se asignan cordenadas aleatorias en el constructor del nodo
    
    for i in range(n):
        for j in range(n):
            if j != i: 
                #Si los nodos son diferentes se calcula la distancia entre ellos
                dist = np.linalg.norm(g.nodes[i].attr["POS"] - g.nodes[j].attr["POS"]) 
                if dist <= r:
                    #Si la distancia es menos o igual al parámetro r, se crea la arista
                    g.addEdge(i,j,f"{i}->{j}")

    
    print(f"Grafo {g.getType()} ha sido creado")
    return g

def graph_BarabasiAlbert(n,d,dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert --   Generates random graph with Barabasi-Albert  model 
    :param n: número de nodos (n > 0) --  number of nodes (n > 0)
    :param d: grado máximo esperado por cada nodo (d > 1) -- maximum degree expected for each node
    :param dirigido: el grafo es dirigido -- directed graph Bool
    :return: grafo generado  -- graph generated
    """
    g = Graph()
    g.type=BARABASI_ALBERT_GRAPH
    g.generator=GENERATOR_NONE
    #Condiciones iniciales
    if n <= 0:
        n = 1
    if d <= 1:
        d=2
    
    #Crear n nodos
    for u in range(n):
        v = np.random.randint(0,u,(1,u))
        g.addNode(u)
        for k in v[0]:
            
            #Grado del nodo
            deg = len(g.nodes[k].attr["NEIGHBORS"]) 

            #Cálculo de probabilidad    
            p = 1 - deg / d

            prob = random.random()
            if prob<= p:
                if k!= u:
                    g.addEdge(u,k,f"{u}->{k}")  

    print(f"Grafo {g.getType()} ha sido creado")
    return g

def graph_DorogovtsevMendes(n,dirigido=False):
    """
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes --  Generates random graph with  Dorogovtsev-Mendes model 
    :param n: número de nodos (n ≥ 3)    -- number of nodes (n ≥ 3)
    :param dirigido: el grafo es dirigido -- directed graph Bool
    :return: grafo generado  -- graph generated
    """
    #Condiciones iniciales
    if n < 3:
        n = 3
    
    #Crear grafo
    g = Graph()
    g.type=DOROGOGOVTSEV_MENDES_GRAPH
    g.generator=GENERATOR_NONE

    #Crear 3 nodos
    for i in range(3):
        g.addNode(i)
    #Formar el triángulo de aristas
    g.addEdge(1,2,"1->2")
    g.addEdge(2,3,"2->3")
    g.addEdge(3,1,"3->1")

    #Si n es mayor a 3 nodos
    if n >3:
        
        for i in range(3,n):
            randomEdge = random.choice(g.getEdges())
            target1, target2 = randomEdge
            g.addNode(i)
            g.addEdge(i,target1,f"{i}->{target1}")
            g.addEdge(i,target2,f"{i}->{target2}")

    print(f"Grafo {g.getType()} ha sido creado")
    return g



def saveGraph_GV(g):
    """
    Genera archivo gv para el grafo g -- Generates gv file for graph g
    :param g: objeto grafo para generar archivo gv  -- graph object to generate gv file 
    """
    #  Tipos de grafo posibles   graph_Type = ["GRID","ERDOS-RENYI","GILBERT","GEOGRAPHIC_SIMPLE","BARABASI-ALBERT","DOROGOVRSEV-MENDES"]
    #Asignación del nombre de archivo gv
    file_name = "files_GV\{}_{}_{}_GRAPH.gv".format(g.getType(),len(g.getNodes()),g.getGenerator())

    if g.type == DIJKSTRA_TREE:  
        with open(file_name, mode="w") as file:
            file.write("digraph my_graph {\n")
            file.writelines(
                [f"{int(e)} [label=nodo_{int(e)}({d})]\n" for e, d in zip(list(g.nodes.keys()), g.ds)])
            file.writelines(
                [f"{e}\n" for e in g.edges.keys()])
            file.write("}")
            print("Grafo guardado")
    else:
            
        #Escritura del archivo gv
        with open(file_name,'w') as file:
            file.write("digraph my_graph {\n")
            for node in g.getNodes():
                file.write("{};\n".format(node))
            for edge in g.edges.keys():
                file.write("{}\n".format(edge))
            file.write("}")
        print("Grafo guardado")
    return 