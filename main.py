import igraph as ig
import numpy as np
import matplotlib.pyplot as plt



n = int(input("Ingrese la dimensión N de la matriz: "))
aristas = ()
matrix = np.zeros((n,n))

def input_matriz(matrix, n):
    print("Matriz de adyacencia")
    aristas_temp = []
    for i in range(n):
        for j in range(n):
            while True:
                try:
                    inp = int(input(f"Existe conexión para el nodo de la fila {i + 1},  columna {j + 1}? (0 -no- o 1 -si-): "))
                except ValueError:
                    print("Número no válido")

                if inp == 1:
                    aristas_temp.append((i,j))
                    
                if inp == 0 or inp == 1:   
                    matrix[i,j] = inp
                    break
                else:
                    print("Ingresar 1 o 0")
     
        aristas_totales = tuple(aristas_temp)
    return matrix, aristas_totales



matrix, aristas = input_matriz(matrix, n)
#Representación matemática
print("Representación matemática")
print("(v,w) = ", aristas)
print("Matriz de adyacencia")
print(matrix)


# Creacion del Grafo
simetrica = np.array_equal(matrix, matrix.T)
diagonal = np.all(np.diag(matrix) == 0)
tipo = ""

if simetrica and diagonal:
    grafo = ig.Graph.Adjacency(matrix, mode="undirected")
    tipo = "no dirigido"
else:
   grafo = ig.Graph.Adjacency(matrix, mode="directed")
   tipo = "dirigido"

grafo["title"] = "Grafo de cuello negro"
grafo.vs["name"] = [str(i) for i in range(grafo.vcount())]

caminosN = grafo.degree()

for i in range(grafo.vcount()):
    print(f"Caminos Nodo {i+1}: {caminosN[i]}")

# caminos = grafo.get_all_simple_paths(0, n-1)

# if grafo.is_dag():
#     ciclos = grafo.fundamental_cycles()
#     print("Ciclos: ", ciclos)



fig, ax = plt.subplots(figsize=(12,12))
ig.plot(
    grafo,
    target=ax,
    layout="circle",
    vertex_size=50,
    vertex_color="blue",
    vertex_frame_width=2.0,
    vertex_frame_color="black",
    vertex_label=grafo.vs["name"],
    vertex_label_size=6,
    edge_width=1,
    edge_color="black",
)

plt.show()

##print(Matrix)








"""vertex = [1,2,3,4,5]
edges = [(1,2),(3,4),(4,5)]

g = gp.Graph(vertex,edges)

print(g)"""