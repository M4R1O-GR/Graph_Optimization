import igraph as ig
import numpy as np
import matplotlib.pyplot as plt


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Número no válido")


def solicitar_dimension():
    while True:
        n = leer_entero("Ingrese la dimensión N de la matriz: ")
        if n > 0:
            return n
        print("La dimensión debe ser mayor a 0")


def crear_matriz(n):
    return np.zeros((n, n))


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
                    continue

                if inp == 1:
                    aristas_temp.append((i, j))

                if inp == 0 or inp == 1:
                    matrix[i, j] = inp
                    break
                else:
                    print("Ingresar 1 o 0")

        aristas_totales = tuple(aristas_temp)
    return matrix, aristas_totales


def mostrar_representacion(n, aristas, matrix):
    print("\n--- REPRESENTACIÓN MATEMÁTICA ---")
    print("Grafo = (v,a)")
    print(f"v = {list(range(1, n + 1))}")
    print(f"a = {aristas}")
    print("\n--- MATRIZ DE ADYACENCIA ---")
    print(matrix)


def crear_grafo(matrix):
    simetrica = np.array_equal(matrix, matrix.T)
    diagonal = np.all(np.diag(matrix) == 0)

    if simetrica and diagonal:
        grafo = ig.Graph.Adjacency(matrix, mode="undirected")
        tipo = "no dirigido"
    else:
        grafo = ig.Graph.Adjacency(matrix, mode="directed")
        tipo = "dirigido"

    grafo["title"] = "Grafo de cuello negro"
    grafo.vs["name"] = [str(i + 1) for i in range(grafo.vcount())]
    return grafo, tipo


def mostrar_tipo(grafo, tipo):
    print(f"\nTipo de grafo: {tipo}")


def mostrar_caminos(grafo, tipo):
    if tipo == "no dirigido":
        caminosN = grafo.degree()
    else:
        caminosN = grafo.degree(mode="out")

    print("\n")
    for i in range(grafo.vcount()):
        print(f"\nCaminos Nodo {i + 1}: {caminosN[i]}")
    print("\n")


def mostrar_ciclos(matrix):
    print("\n")
    for i in range(len(matrix)):
        ciclos = int(matrix[i, i])
        print(f"Ciclos Nodo {i + 1}: {ciclos}")
    print("\n")


def mostrar_vecinos(grafo):
    for i in range(grafo.vcount()):
        vecinos = grafo.neighbors(i)
        vecinos = [v + 1 for v in vecinos if v != i]
        print(f"Vecinos Nodo {i + 1}: {vecinos}")


def asignar_pesos(grafo, tipo):
    print("\n--- PESO DE ARISTAS = 1 ---")
    matriz_pesos = np.zeros((grafo.vcount(), grafo.vcount()))
    pesos_grafo = []

    for edge in grafo.es:
        u = edge.source
        v = edge.target
        peso = 1.0
        matriz_pesos[u, v] = peso
        if tipo == "no dirigido":
            matriz_pesos[v, u] = peso
        pesos_grafo.append(peso)

    grafo.es["label"] = [str(int(p)) for p in pesos_grafo]
    return matriz_pesos


def seleccionar_ruta(n):
    print("\n--- SELECCIÓN DE RUTA ---")
    while True:
        origen = leer_entero(f"Ingrese el nodo de ORIGEN (1 a {n}): ") - 1
        destino = leer_entero(f"Ingrese el nodo de DESTINO (1 a {n}): ") - 1
        if 0 <= origen < n and 0 <= destino < n:
            return origen, destino
        print(f"Los nodos deben estar entre 1 y {n}")


def algoritmo_dijkstra(matriz_p, inicio, dim):
    distancias = [float('inf')] * dim
    distancias[inicio] = 0
    visitados = [False] * dim
    previos = [-1] * dim

    for _ in range(dim):
        min_dist = float('inf')
        u = -1
        for i in range(dim):
            if not visitados[i] and distancias[i] < min_dist:
                min_dist = distancias[i]
                u = i

        if u == -1: break
        visitados[u] = True

        for v in range(dim):
            if matriz_p[u, v] != 0 and not visitados[v]:
                alt = distancias[u] + matriz_p[u, v]
                if alt < distancias[v]:
                    distancias[v] = alt
                    previos[v] = u
    return distancias, previos


def algoritmo_bellman_ford(matriz_p, inicio, dim):
    distancias = [float('inf')] * dim
    distancias[inicio] = 0
    previos = [-1] * dim

    lista_aristas = [(u, v, matriz_p[u, v]) for u in range(dim) for v in range(dim) if matriz_p[u, v] != 0]

    for _ in range(dim - 1):
        for u, v, p in lista_aristas:
            if distancias[u] != float('inf') and distancias[u] + p < distancias[v]:
                distancias[v] = distancias[u] + p
                previos[v] = u

    for u, v, p in lista_aristas:
        if distancias[u] != float('inf') and distancias[u] + p < distancias[v]:
            print("¡Alerta! El grafo contiene un ciclo de peso negativo.")
            return distancias, previos

    return distancias, previos


def reconstruir_ruta(destino, previos):
    ruta = []
    actual = destino
    while actual != -1:
        ruta.insert(0, actual)
        actual = previos[actual]
    return ruta


def mostrar_resultado_dijkstra(ruta, costo):
    print("\n--- RESULTADO: DIJKSTRA ---")
    if ruta:
        ruta_texto = " -> ".join([str(nodo + 1) for nodo in ruta])
        print(f"Nodos de la ruta más corta: {ruta_texto}")
        print(f"Costo total (según Dijkstra): {int(costo)}")
    else:
        print("No existe una ruta viable entre el origen y el destino seleccionados.")


def mostrar_resultado_bellman_ford(ruta, costo):
    print("\n--- RESULTADO: BELLMAN-FORD ---")
    if ruta:
        ruta_texto = " -> ".join([str(nodo + 1) for nodo in ruta])
        print(f"Nodos de la ruta más corta: {ruta_texto}")
        print(f"Costo total (según Bellman-Ford): {int(costo)}")
    else:
        print("No existe una ruta viable entre el origen y el destino seleccionados.")


def preparar_visualizacion(grafo, ruta):
    colores_vertices = ["blue"] * grafo.vcount()
    colores_aristas = ["black"] * grafo.ecount()
    grosores_aristas = [1] * grafo.ecount()

    for nodo in ruta:
        colores_vertices[nodo] = "red"

    for i in range(len(ruta) - 1):
        u, v = ruta[i], ruta[i + 1]
        try:
            eid = grafo.get_eid(u, v)
            colores_aristas[eid] = "red"
            grosores_aristas[eid] = 3.0
        except ig.InternalError:
            pass

    return colores_vertices, colores_aristas, grosores_aristas


def graficar_grafo(grafo, ruta):
    colores_vertices, colores_aristas, grosores_aristas = preparar_visualizacion(grafo, ruta)

    fig, ax = plt.subplots(figsize=(6, 6))
    ig.plot(
        grafo,
        target=ax,
        layout="circle",
        vertex_size=50,
        vertex_color=colores_vertices,
        vertex_frame_width=2.0,
        vertex_frame_color="black",
        vertex_label=grafo.vs["name"],
        vertex_label_size=12,
        edge_width=grosores_aristas,
        edge_color=colores_aristas,
        edge_label=grafo.es["label"],
        edge_label_size=10,
        edge_label_color="red"
    )

    plt.show()
