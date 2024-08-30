#kruskal x prim

import heapq
import time

# Algoritmo de Prim
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

# Algoritmo de Kruskal
def kruskal_mst(graph):
    # Helper function to find the root of a set
    def find(parent, i):
        if parent[i] == i:
            return i
        else:
            root = find(parent, parent[i])
            parent[i] = root
            return root

    # Helper function to union two sets
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)

        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    edges = []
    for frm, neighbors in graph.items():
        for to, cost in neighbors.items():
            if (to, frm, cost) not in edges:
                edges.append((frm, to, cost))

    # Sort edges by cost
    edges.sort(key=lambda x: x[2])

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    mst = []
    for frm, to, cost in edges:
        if find(parent, frm) != find(parent, to):
            union(parent, rank, frm, to)
            mst.append((frm, to, cost))

    return mst

# Definindo o grafo a partir da imagem
graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

# Medindo o tempo de execução do Algoritmo de Prim
start_time = time.time()
mst_prim = prim_mst(graph, 'D')
prim_time = time.time() - start_time

print("Arestas da Árvore Geradora Mínima (Prim):")
for edge in mst_prim:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")

print(f'\nTempo de execução do Algoritmo de Prim: {prim_time:.20f} segundos')	



# Medindo o tempo de execução do Algoritmo de Kruskal
start_time = time.time()
mst_kruskal = kruskal_mst(graph)
kruskal_time = time.time() - start_time


print("\nArestas da Árvore Geradora Mínima (Kruskal):")
for edge in mst_kruskal:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")


print(f'\nTempo de execução do Algoritmo de Kruskal: {kruskal_time:.20f} segundos')	

'''if prim_time < kruskal_time:
    diferenca_percentual = (kruskal_time - prim_time) / kruskal_time * 100

    print(f'\nO Algoritmo de Prim foi mais rápido em {diferenca_percentual:.2f}%')
else:
    diferenca_percentual = (prim_time - kruskal_time) / prim_time * 100
    print(f'\nO Algoritmo de Kruskal foi mais rápido em {diferenca_percentual:.2f}%')'''



