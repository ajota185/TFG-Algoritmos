from anytree import Node, LevelOrderGroupIter, RenderTree, exporter

def representaciones_de_M(coins,nodo):
    
    if(nodo.name==0):
        return {()}
    #     return nodo
    
    representaciones = set()

    for coin in coins:
        if(coin <= nodo.name):
            nuevo_nodo = Node(nodo.name-coin, parent=nodo)
            monedas_restantes = representaciones_de_M(coins,nuevo_nodo)
            for monedas in monedas_restantes:
                representacion = tuple(sorted((coin,) + monedas))
                representaciones.add(representacion)
    
    return representaciones
    

def algoritmo_cambio_moneda_arbol(coins,N):
    root = Node(N)
    return representaciones_de_M(coins,root)



# M=12
# coins = [3,5,7]
# root = Node(M)
# representaciones_lista = representaciones_de_M(coins,root)


# for pre, fill, node in RenderTree(root):
#     print("%s%d" % (pre, node.name))

# exporter.UniqueDotExporter(root,
#             edgeattrfunc=lambda parent, child: "style=bold,label=%d" % (parent.name - child.name)
# ).to_picture("ejemplo_arbol.png") 

# for monedas in lista_monedas:
#     monedas.sort()

# for i in range(len(representaciones_lista)):
#     # monedas = tuple(sorted(monedas))
#     representaciones_lista[i]=tuple(sorted(representaciones_lista[i]))

# representaciones_conjunto = set(representaciones_lista)
# print("El número de representaciones posibles de M=" + str(M) + " es " + str(len(representaciones_lista)))
# lista_monedas_sin_repetidos = []

# # Elimino las representaciones repetidas
# for moneda in lista_monedas:
#     # Convertir la lista en una tupla para hacerla hashable
#     moneda_tupla = tuple(moneda)
#     if moneda_tupla not in conjunto_monedas:
#         conjunto_monedas.add(moneda_tupla)
#         lista_monedas_sin_repetidos.append(moneda)


# print(lista_monedas_sin_repetidos)

# M_str = str(M)
# n_representaciones_str = str(len(lista_monedas_sin_repetidos))
# print("El número de representaciones posibles de M=" + M_str + " es " + n_representaciones_str)

