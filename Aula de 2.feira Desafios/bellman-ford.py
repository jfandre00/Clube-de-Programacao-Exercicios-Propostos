class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.edges = []    # Lista para armazenar as arestas

    # Função para adicionar arestas
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # Função para implementar o algoritmo de Bellman-Ford
    def bellman_ford(self, src):
        # Passo 1: Inicializar distâncias de todos os vértices como infinito
        dist = [float("inf")] * self.V
        dist[src] = 0  # A distância do vértice origem para ele mesmo é sempre 0

        # Passo 2: Relaxar todas as arestas |V| - 1 vezes
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Passo 3: Verificar ciclos de peso negativo
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("O grafo contém um ciclo de peso negativo")
                return

        # Imprimir as distâncias calculadas
        self.print_solution(dist)

    def print_solution(self, dist):
        print("Distâncias do vértice origem:")
        for i in range(self.V):
            print(f"Vértice {i} \t Distância: {dist[i]}")

# Número de vértices no grafo
g = Graph(6)

# Adicionar as arestas do grafo
g.add_edge(0, 1, 9)   # A → B
g.add_edge(0, 2, 7)   # A → C
g.add_edge(2, 3, 2)   # C → D
g.add_edge(3, 1, -3)  # D → B
g.add_edge(3, 4, -2)  # D → E
g.add_edge(4, 5, -2)  # E → F
g.add_edge(5, 1, 2)   # F → B
g.add_edge(1, 4, 2)   # B → E

# Escolher o vértice de origem como 0 (A)
g.bellman_ford(0)