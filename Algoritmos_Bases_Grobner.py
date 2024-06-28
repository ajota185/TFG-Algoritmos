from sympy import Poly, groebner, symbols, ring, QQ
# # Calculo S-polinomio de dos polinomios
# def S_Polinomio(f1,f2):
#     LMf1 = f1.leading_monom()
#     LTf1 = f1.leading_term()
#     LMf2 = f2.leading_monom()
#     LTf2 = f2.leading_term()
#     M = LMf1.lcm(LMf2)
#     # div1 = M.div(LTf1)[0]
#     # div2 = M.div(LTf2)[0]
#     S = M.div(LTf1)[0]*f1 - M.div(LTf2)[0]*f2
#     return S

# # Algoritmo de Buchberger para el cálculo 
# # de una base de Gröbner a partir de 
# # un Ideal generado por F=[g1,...,gs]
# def Algoritmo_Buchberger(F):
#     G = list(set(F))

#     # Inicializo P con todos los posibles pares de polinomios
#     P = []
#     for i in range(len(G)):
#         j=i+1
#         while(j<len(G)):
#             if i!=j:
#                 P.append([G[i],G[j]])
#             j=j+1
#     print("P = " + str(P))
    
#     iteracion=1
#     # Hago las iteraciones del algoritmo
#     while(P != []):
#         print("Iteracion " + str(iteracion))
#         par = P.pop()
#         print("\tPar = " + str(par))
#         print("\tS("+str(par[0])+","+str(par[1])+") = " + str(S_Polinomio(par[0],par[1])))
#         h = S_Polinomio(par[0],par[1]).div(G)[1]
#         print("\th = " + str(h))
#         if h!=0:
#             for u in G:
#                 P.append([u,h])
#             G.append(h)
#         print("\tG = " + str(G))
#         print("\tP = " + str(P))
#         iteracion +=1
#     return G


# # A partir de una base de Gröbner 
# # G = [g_1,...g_s]
# # calculo base de Göbner minimal
# def Base_Minimal(G):
#     M = list(G)
#     i=0
#     while i < len(M):
#         print("Iteración " + str(i+1))
#         j=0
#         LMg = M[i].leading_monom()
#         print("\tLM(g_i) = " + str(LMg))
#         elimino=False
#         while j<len(M) and elimino==False:
#             if i != j:
#                 LMh = M[j].leading_monom()
#                 print("\t\tLM(g_j) = " + str(LMh))
#                 res = LMg.div(LMh)[1]
#                 print("\t\tres = " + str(res))
#                 if LMg.div(LMh)[1]==0:
#                     print("\t\tElimino LM(g_i)")
#                     M.remove(M[i])
#                     elimino=True
#             j+=1
#         if not elimino:
#             i+=1
#         print("\tM = " + str(M))
#     print("Dividiendo los LC(g_i)")
#     for i in range(len(M)):
#         LCm = M[i].coeffs()[0]
#         M[i] = M[i]/LCm
#     print("M = " + str(M))
#     return M

# # A partir de una base de Gröbner minimal
# # G = [g_1,...g_s]
# # calculo base de Göbner reducida
# def Base_reducida(G):
#     H = list(G)
#     for i in range(len(G)):
#         print("Iteración " + str(i+1))
#         g = H.pop(0)
#         print("\tg = " + str(g))
#         print("\tH = " + str(H))
#         h = g.div(H)[1]
#         print("\th = " + str(h))
#         H.append(h)
#     print("H = " + str(H))
#     return H


# Métodos sin imprimir iteraciones
# Calculo S-polinomio de dos polinomios
def S_Polinomio(f1,f2):
    LMf1 = f1.leading_monom()
    LTf1 = f1.leading_term()
    LMf2 = f2.leading_monom()
    LTf2 = f2.leading_term()
    M = LMf1.lcm(LMf2)
    # div1 = M.div(LTf1)[0]
    # div2 = M.div(LTf2)[0]
    S = M.div(LTf1)[0]*f1 - M.div(LTf2)[0]*f2
    return S

# Algoritmo de Buchberger para el cálculo 
# de una base de Gröbner a partir de 
# un Ideal generado por F=[g1,...,gs]
def Algoritmo_Buchberger(F):
    G = list(set(F))

    # Inicializo P con todos los posibles pares de polinomios
    P = []
    for i in range(len(G)):
        j=i+1
        while(j<len(G)):
            if i!=j:
                P.append([G[i],G[j]])
            j=j+1
    
    iteracion=1
    # Hago las iteraciones del algoritmo
    while(P != []):
        par = P.pop()
        h = S_Polinomio(par[0],par[1]).div(G)[1]
        if h!=0:
            for u in G:
                P.append([u,h])
            G.append(h)
    return G


# A partir de una base de Gröbner 
# G = [g_1,...g_s]
# calculo base de Göbner minimal
def Base_Minimal(G):
    M = list(G)
    i=0
    while i < len(M):
        j=0
        LMg = M[i].leading_monom()
        elimino=False
        while j<len(M) and elimino==False:
            if i != j:
                LMh = M[j].leading_monom()
                res = LMg.div(LMh)[1]
                if res==0:
                    M.remove(M[i])
                    elimino=True
            j+=1
        if not elimino:
            i+=1
    for i in range(len(M)):
        LCm = M[i].coeffs()[0]
        M[i] = M[i]/LCm
    return M

# A partir de 
# calculo base de Göbner reducida
# calculo base de Göbner reducida base de Gröbner minimal

# calculo base de Göbner reducida# calculo base de Göbner reducida
# calculo base de Göbner reducida
# calculo base de Göbner reducida
def Base_reducida(G):
    H = list(G)
    for i in range(len(G)):
        g = H.pop(0)
        h = g.div(H)[1]
        H.append(h)
    return H

def algoritmo_cambio_moneda_Bases_Grobner(A,N):
    variables = ['x','t']
    variables += [f'v{i}' for i in range(1, len(A)+2)]
    variables += [f'w{i}' for i in range(1, len(A)+2)]
    vars = symbols(variables)
    num_vars = len(vars)
    x=vars[0]
    t=vars[1]
    v=vars[2:len(A)+3]
    w=vars[len(A)+3:]

    I=list()
    for i in range(len(A)):
        I.append(w[i]*x**A[i]-v[i])
    I.append(w[len(A)]*t**N-v[len(A)])
    I.append(x*t-1)
    # print("I = " + str(I))
    B = list(groebner(I,method='f5b'))
    # print("B = " + str(I))
    representaciones = list()
    for b in B:
        pol = Poly(b,vars)
        m1 = pol.monoms()[0]
        m2 = pol.monoms()[1]
        m1_w = m1[len(A)+3:]
        m2_v = m2[2:len(A)+3]
        if(m1[0]==0 and m1[1]==0 and all(x==0 for x in m1_w) and m2[0]==0 and m2[1]==0 and all(x==0 for x in m2_v)):
            i=2
            termino=False
            while (i < len(v)+2 and termino==False):
                if(m1[i]!=m2[i+len(v)]):
                    termino=True
                elif (i==len(v)+1 and (m1[i]!=1 or m2[i+len(v)]!=1)):
                    termino=True
                i+=1
            if (termino==False):
                representaciones.append(m1[2:len(A)+2])
            # print(pol.expr)
            # print(m1)
            # print(m2)
    return representaciones

# algoritmo_cambio_moneda_Bases_Grobner([3, 7, 9],10)
