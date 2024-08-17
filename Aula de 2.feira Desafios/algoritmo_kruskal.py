# Implementação da estrutura Union-Find com compressão de caminhos e união por # classificação
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compressão de caminho
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # União por classificação
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Função para executar o Algoritmo de Kruskal
def kruskal(vertices, edges):
    # Ordenar as arestas por peso
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(len(vertices))
    mst = []

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst

# Exemplo de uso
if __name__ == "__main__":
    # Vértices do grafo
    vertices = [0, 1, 2, 3]

    # Arestas do grafo (u, v, peso)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4),
        (1, 2, 8)
    ]

    mst = kruskal(vertices, edges)
    print("Arestas da árvore geradora mínima:")
    for u, v, weight in mst:
        print(f"Aresta ({u}, {v}) com peso {weight}")