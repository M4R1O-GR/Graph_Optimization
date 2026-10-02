import main

estado = {
    "n": None,
    "matrix": None,
    "aristas": (),
    "grafo": None,
    "tipo": "",
    "matriz_pesos": None,
    "origen": None,
    "destino": None,
    "ruta": [],
}


def hay_grafo():
    return estado["grafo"] is not None


def advertir_sin_grafo():
    if hay_grafo():
        return True
    print("Primero ingrese la matriz de adyacencia (opción 1).")
    return False


def opcion_ingresar_matriz():
    n = main.solicitar_dimension()
    matrix = main.crear_matriz(n)
    matrix, aristas = main.input_matriz(matrix, n)
    grafo, tipo = main.crear_grafo(matrix)
    matriz_pesos = main.asignar_pesos(grafo, tipo)

    estado.update({
        "n": n,
        "matrix": matrix,
        "aristas": aristas,
        "grafo": grafo,
        "tipo": tipo,
        "matriz_pesos": matriz_pesos,
        "origen": None,
        "destino": None,
        "ruta": [],
    })
    print("\nGrafo cargado correctamente.")


def opcion_ver_caminos():
    if not advertir_sin_grafo():
        return
    main.mostrar_tipo(estado["grafo"], estado["tipo"])
    main.mostrar_caminos(estado["grafo"], estado["tipo"])
    main.mostrar_vecinos(estado["grafo"])


def opcion_ver_ciclos():
    if not advertir_sin_grafo():
        return
    main.mostrar_ciclos(estado["matrix"])


def opcion_dijkstra():
    if not advertir_sin_grafo():
        return
    origen, destino = main.seleccionar_ruta(estado["n"])
    distancias, previos = main.algoritmo_dijkstra(estado["matriz_pesos"], origen, estado["n"])
    ruta = main.reconstruir_ruta(destino, previos)

    estado.update({"origen": origen, "destino": destino, "ruta": ruta})
    main.mostrar_resultado_dijkstra(ruta, distancias[destino])


def opcion_bellman_ford():
    if not advertir_sin_grafo():
        return
    origen, destino = main.seleccionar_ruta(estado["n"])
    distancias, previos = main.algoritmo_bellman_ford(estado["matriz_pesos"], origen, estado["n"])
    ruta = main.reconstruir_ruta(destino, previos)

    estado.update({"origen": origen, "destino": destino, "ruta": ruta})
    main.mostrar_resultado_bellman_ford(ruta, distancias[destino])


def opcion_ver_grafo():
    if not advertir_sin_grafo():
        return
    if not estado["ruta"]:
        print("Aún no se calcula una ruta; se mostrará el grafo sin resaltar.")
    main.graficar_grafo(estado["grafo"], estado["ruta"])


def opcion_ver_representacion():
    if not advertir_sin_grafo():
        return
    main.mostrar_representacion(estado["n"], estado["aristas"], estado["matrix"])


def menu():
    while True:
        print("1. Ingresar matriz de adyacencia")
        print("2. Ver caminos del grafo")
        print("3. Ver ciclos del grafo")
        print("4. Camino mas corto entre dos nodos (Dijkstra)")
        print("5. Camino mas corto entre dos nodos (Bellman-Ford)")
        print("6. Ver grafo")
        print("7. Visualizar representación matematica y matriz de adyacencia")
        print("8. Salir")
        print()

        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        match(opc):
            case 1:
                opcion_ingresar_matriz()
            case 2:
                opcion_ver_caminos()
            case 3:
                opcion_ver_ciclos()
            case 4:
                opcion_dijkstra()
            case 5:
                opcion_bellman_ford()
            case 6:
                opcion_ver_grafo()
            case 7:
                opcion_ver_representacion()
            case 8:
                break
            case _:
                print("Opción no válida.")


menu()
