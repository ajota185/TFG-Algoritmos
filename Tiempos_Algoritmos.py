import time
from Algoritmo_Arbol_Recursivo import algoritmo_cambio_moneda_arbol
from Algoritmo_Programacion_Dinamica import algoritmo_cambio_moneda_prog_din
from Algoritmo_Round_Robin import algoritmo_cambio_moneda_RR
from Algoritmos_Bases_Grobner import algoritmo_cambio_moneda_Bases_Grobner


def medir_tiempo(algoritmo, monedas, cantidad):
    start_time = time.time()
    resultado = algoritmo(monedas, cantidad)
    end_time = time.time()
    # print("Tiempo:" + str(end_time - start_time))
    return end_time - start_time, resultado

# conjunto_repre_coins = [
#     [4,9],
#     [2, 3, 8],
#     [2, 3, 5, 7],
#     [5, 10, 20, 50, 54],
#     [8, 16, 24, 32, 40, 41],
#     [6, 9, 12, 15, 22, 44, 56],
#     [7, 10, 15, 18, 27, 29, 45, 49],
#     [33, 46, 52, 57, 61, 88, 93, 99, 100]
# ]

test_cases = [
    (25, [[6, 7], [3, 7, 9], [2, 6, 8, 9], [4, 5, 7, 8, 9], [2, 3, 4, 6, 8, 9], [3, 4, 5, 7, 8, 9, 10], [2, 3, 5, 6, 8, 9, 10, 12]]),
    (50, [[3, 11], [7, 9, 20], [6, 10, 15, 25], [8, 12, 20, 30, 50], [4, 7, 13, 17, 23, 29],[3, 8, 19, 22, 28, 37, 45], [2, 5, 10, 18, 22, 35, 42, 47]]),
    (100, [[7, 26], [6, 11, 20], [7, 14, 28, 35], [9, 18, 27, 45, 60], [4, 17, 19, 23, 29, 31], [3, 12, 15, 28, 35, 41, 50], [7, 8, 13, 22, 27, 31, 45, 55]]),
    (200, [[4, 50], [15, 30, 60], [14, 25, 50, 75], [9, 18, 27, 45, 90], [8, 17, 29, 41, 63, 78], [7, 13, 19, 31, 45, 67, 81], [6, 11, 22, 33, 55, 67, 89, 100]])
]


test_cases_base_grobner = [
    # (25, [[6, 7], [3, 7, 9]]),
    # (50, [[3,11]]),
    # (100, [[7, 26]]),
    (200, [[15, 30, 60]])
]

test_cases_N_mediano = [
    (5673, [[33, 455, 746, 1100]]),
    (10067, [[11, 638, 1054, 4009]]),
    (51765, [[54, 4569, 10651, 13657]]),
    (100000, [[89, 6372, 7219, 25987]])
]

conjunto_repre_coins_10 = [
    [10,19],
    [2,6,10],
    [3,5,7,8],
    [3,5,7,9,10]
]

conjunto_repre_coins_20 = conjunto_repre_coins_10 + [
    [4,7,9,5,2,7]


]

# N=20
# conjunto_repre_coins_20 = [
#     [2,5],
#     [2,6,10],
#     [2,5,7,9,10]
# ]
# algoritmos = [algoritmo_cambio_moneda_arbol, algoritmo_cambio_moneda_prog_din, algoritmo_cambio_moneda_RR, algoritmo_cambio_moneda_Bases_Grobner]
# algoritmos = [algoritmo_cambio_moneda_Bases_Grobner]
algoritmos = [algoritmo_cambio_moneda_prog_din ,algoritmo_cambio_moneda_RR]
# N=10
# while N<=50:
#     print("N = "+str(N))
#     for coins in conjunto_repre_coins:
#         print("  Algoritmo en Arbol")
#         for aloritmo in algoritmos:

#         medir_tiempo(algoritmo_cambio_moneda_arbol, coins, N)
#         medir_tiempo(algoritmo_cambio_moneda_prog_din, coins, N)
#         medir_tiempo(algoritmo_cambio_moneda_RR, coins, N)
#     N+=10

# resultados = []
# N=20
resultadoStr = ""
# Ejecutar las pruebas y recopilar los resultados
for N, group_coins in test_cases_N_mediano:
    resultadoStr += "N = " + str(N) + "\n"
    for i, algoritmo in enumerate(algoritmos):
        print("Algoritmo "+str(i) + ":")
        for coins in group_coins:
#            print(f"\tTest case N={N}, N_monedas={len(coins)}")
            # if (len(coins)>6 and i==0 and N==200):
            #     tiempo = 0.000000
            # else:
            tiempo, resultado = medir_tiempo(algoritmo, coins, N)
#            print(f"\t{tiempo:.6f}")
            # print(resultado)
            resultadoStr += f"{tiempo:.6f}\t"
            # fila = f"{N}\t{monedas}\tAlgoritmo {i+1}\t{tiempo:.6f}\t{resultado}\n"
            # resultados.append(fila)
        resultadoStr += "\n"
    # resultadoStr += "\n"

print(resultadoStr)
# resultados_completos = "".join(resultados)
# print(resultados_completos)

# Guardar los resultados en un archivo de texto
#with open("resultados_tiempos_2.txt", "w") as file:
#    file.write(resultadoStr)

# print(f"Algoritmo 1: Tiempo = {tiempo1}s, Resultado = {resultado1}")
