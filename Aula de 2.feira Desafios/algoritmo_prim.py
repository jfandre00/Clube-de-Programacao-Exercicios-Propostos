import heapq

def prim_mst(graph, start):
    mst = []
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    return mst

# Definindo o grafo a partir da imagem (pdf da aula 13)
#Q: o que é algoritmo de prim?
#A: O algoritmo de Prim é um algoritmo guloso que encontra uma árvore geradora mínima para um grafo ponderado conexo.


graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

# Executando o algoritmo de Prim partindo de D
mst = prim_mst(graph, 'D')

# Imprimindo o resultado
print("Arestas da Árvore Geradora Mínima:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")