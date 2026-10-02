from re import match

import main

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
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break
            case _:
                print("Opción no válida.")
