from math import gcd

def imprimirMatriz(M):
    M_str=""
    for i in range(len(M)):
        for j in range(len(M[i])):
            M_str += str(M[i][j])
            if j<len(M[i])-1:
                M_str +="\t"
        if i<len(M)-1:
            M_str += "\n"
    print(M_str)

def algoritmo_round_robin_ERT(A):
    n = len(A)
    a1 = A[0]

    # Paso 1: Inicializar todo a inf expecto la primera fila que va a 0
    ERT = [[float('inf')] * n for _ in range(a1)]
    for j in range(n):
        ERT[0][j] = 0

    # Paso 2: Bucle a través de i desde 2 hasta n
    for i in range(1, n):
        ai = A[i]
        d = gcd(a1, ai)
        
        # Paso 4: Bucle a través de p desde 0 hasta d - 1
        for p in range(d):
            # Paso 5: Encontrar n = min{ERT[q][i-1] | q mod d = p, 0 ≤ q ≤ a1 − 1}
            min_n = float('inf')
            for q in range(a1):
                if q % d == p and ERT[q][i-1] < min_n:
                    min_n = ERT[q][i-1]
            
            if min_n < float('inf'):
                # Paso 6: Repetir a1 / d - 1 veces
                for _ in range(a1 // d - 1):
                    min_n += ai
                    r = min_n % a1
                    
                    # Paso 8: Actualizar ERT[r][i]
                    if min_n < ERT[r][i-1]:
                        ERT[r][i] = min_n
                    else:
                        ERT[r][i] = ERT[r][i-1]
                        min_n = ERT[r][i-1]
    return ERT

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

def algoritmo_cambio_moneda_RR_local(N, i, c, monedas, repre, ERT):
    if i == 0:
        c[0] = N // monedas[0]
        repre.append(c)
        return
    
    mcm = lcm(monedas[0], monedas[i])
    l = mcm // monedas[i]
    
    for j in range(l):
        c[i] = j
        m = N - j * monedas[i]
        
        r = m % monedas[0]
        cota_inf = ERT[r][i-1]
        
        while m >= cota_inf:
            algoritmo_cambio_moneda_RR_local(m, i - 1, c[:], monedas, repre, ERT)
            m -= mcm
            c[i] += l

def algoritmo_cambio_moneda_RR(monedas, N):
    n_monedas = len(monedas)
    c = [0] * n_monedas
    representaciones = list()
    ERT = algoritmo_round_robin_ERT(monedas)
    algoritmo_cambio_moneda_RR_local(N, n_monedas-1, c, monedas, representaciones, ERT)
    return representaciones

# print(len(algoritmo_cambio_moneda_RR([7, 13, 19, 31, 45, 67, 81],200)))
# print(len(algoritmo_cambio_moneda_RR([6, 11, 22, 33, 55, 67, 89, 100],200)))

# Example usage
# monedas = [5, 7, 9, 11]  # Example list of integers
# n_monedas = len(monedas)
# N = 30  # Ejemplo de masa
# c = [0] * n_monedas  # Inicialización de la composición

# ERT = algoritmo_round_robin_ERT(monedas)
# imprimirMatriz(ERT)
# representaciones = list()
# algoritmo_cambio_moneda_RR(N, n_monedas-1, c, monedas, representaciones, ERT)
# print(representaciones)

# print("Resultado array n:", RT)
# ERT = algoritmo_round_robin_ERT(a)

# 
# for i in range(a[0]):
#     for j in range(len(a)):
#         ERT_str += str(ERT[j][i]) + "\t"
#     ERT_str += "\n"
# print(ERT_str)















# from functools import reduce
# from math import gcd

# def lcm(a, b):
#     return a * b // gcd(a, b)

# def lcm_list(numbers):
#     return reduce(lcm, numbers)


# def find_all(M, i, c):
#     if i == 1:
#         c[0] = M // a[0]
#         print(c)
#         return
    
#     lcm = lcm_list(a[:i])
#     l = lcm // a[i-1]

#     for j in range(l):
#         ci = j
#         m = M - j * a[i-1]

#         r = m % a[0]
#         lbound = math.ceil(r**(1/(i-1)))

#         while m >= lbound:
#             find_all(m, i-1, c)
#             m -= lcm
#             ci += l

# a = [2, 3, 5]  # Valores de a1, a2, a3, etc.
# M = 30  # Valor de M
# c = [0] * len(a)

# find_all(M, len(a), c)