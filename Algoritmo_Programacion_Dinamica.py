# def cambio_monedas(monedas, cantidad):

#     # Inicializar tabla de soluciones
#     n_monedas = len(monedas)
#     tabla = [[0 for _ in range(cantidad + 1)] for _ in range(n_monedas + 1)]

#     # Casos base:
#     # - Si la cantidad es 0, hay una sola solución (sin monedas)
#     for i in range(n_monedas + 1):
#         tabla[i][0] = 1

#     # - Si la cantidad es mayor que la denominación de la moneda actual, no hay soluciones
#     for j in range(1, cantidad + 1):
#         for i in range(1, n_monedas + 1):
#             if monedas[i - 1] > j:
#                 tabla[i][j] = tabla[i - 1][j]
#             else:
#                 # Soluciones incluyendo la moneda actual:
#                 #     - Usar la moneda actual una vez y el resto con las monedas anteriores
#                 #     - No usar la moneda actual y usar las monedas anteriores
#                 soluciones_con_moneda = tabla[i][j - monedas[i - 1]]
#                 soluciones_sin_moneda = tabla[i - 1][j]
#                 tabla[i][j] = soluciones_con_moneda + soluciones_sin_moneda

#     # Retornar el número de soluciones para la cantidad y todas las monedas
#     return tabla[n_monedas][cantidad]

                

# Ejemplo de uso
# monedas = [3, 2, 1]    # Denominaciones de monedas
# cantidad = 4    # Cantidad total que se desea obtener

# numero_combinaciones = cambio_monedas(monedas, cantidad)
# print(f"Número de combinaciones de monedas para obtener {cantidad}: {numero_combinaciones}")

# def cambio_monedas_representaciones(monedas, cantidad):
#     # Inicializar tabla de soluciones y tabla de representaciones
#     n_monedas = len(monedas)
#     tabla_soluciones = [[0 for _ in range(cantidad + 1)] for _ in range(n_monedas + 1)]
#     tabla_representaciones = [[[] for _ in range(cantidad + 1)] for _ in range(n_monedas + 1)]

#     # Casos base:
#     # - Si la cantidad es 0, hay una sola representación (sin monedas)
#     for i in range(n_monedas + 1):
#         tabla_representaciones[i][0] = [[]]

#     # - Si la cantidad es mayor que la denominación de la moneda actual, no hay representaciones
#     for j in range(1, cantidad + 1):
#         for i in range(1, n_monedas + 1):
#             if monedas[i - 1] > j:
#                 tabla_representaciones[i][j] = tabla_representaciones[i - 1][j]
#             else:
#                 # Representaciones incluyendo la moneda actual:
#                 #     - Usar la moneda actual una vez y el resto con las monedas anteriores
#                 representaciones_con_moneda = [
#                         representacion + [monedas[i - 1]]
#                         for representacion in tabla_representaciones[i][j - monedas[i - 1]]
#                 ]
#                 # Representaciones sin la moneda actual:
#                 representaciones_sin_moneda = tabla_representaciones[i - 1][j]
#                 tabla_representaciones[i][j] = representaciones_con_moneda + representaciones_sin_moneda

#     # Retornar la lista de representaciones para la cantidad y todas las monedas
#     return tabla_representaciones[n_monedas][cantidad]

def algoritmo_cambio_moneda_prog_din(monedas, cantidad):
    # Inicializar la tabla de representaciones
    n_monedas = len(monedas)
    tabla_representaciones = [[[] for _ in range(cantidad + 1)] for _ in range(n_monedas + 1)]

    # Caso base: si la cantidad es 0, hay una sola representación (sin monedas)
    for i in range(n_monedas + 1):
        tabla_representaciones[i][0] = [[]]

    # Llenar la tabla de representaciones
    for j in range(1, cantidad + 1):
        for i in range(1, n_monedas + 1):
            if monedas[i - 1] <= j:
                # Representaciones incluyendo la moneda actual
                representaciones_con_moneda = [
                    representacion + [monedas[i - 1]]
                    for representacion in tabla_representaciones[i][j - monedas[i - 1]]
                ]
                # Representaciones sin la moneda actual
                representaciones_sin_moneda = tabla_representaciones[i - 1][j]
                tabla_representaciones[i][j] = representaciones_sin_moneda + representaciones_con_moneda
            else:
                tabla_representaciones[i][j] = tabla_representaciones[i - 1][j]

    # Retornar la lista de representaciones para la cantidad y todas las monedas
    return tabla_representaciones[n_monedas][cantidad]
# Ejemplo de uso
# monedas = [5,8]    # Denominaciones de monedas
# cantidad = 100    # Cantidad total que se desea obtener

# representaciones_monedas = cambio_monedas_representaciones(monedas, cantidad)
# print(f"Representaciones de {cantidad} con las monedas {monedas}:")
# for representacion in representaciones_monedas:
#     print(representacion)
