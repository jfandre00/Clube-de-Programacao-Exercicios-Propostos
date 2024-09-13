import heapq

def dijkstra(graph, start):
    # Inicialização das distâncias e caminhos
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}
				                       # Dicionário para armazenar o caminho

    # Inicialização da fila de prioridade
    priority_queue = [(0, start)]

    while priority_queue:
        # Extração do vértice com menor distância
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Se a distância atual é maior que a distância armazenada, ignore
        if current_distance > distances[current_vertex]:
            continue

        # Relaxamento das arestas
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Se a nova distância é menor, atualize
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex  # Atualiza o caminho
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def get_path(previous_nodes, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()  # O caminho é construído de trás para frente
    return path

# Definição do grafo
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 4, 'D': 2, 'E': 4},
    'C': {'A': 1, 'B': 2, 'D': 5, 'E': 5},
    'D': {'B': 2, 'C': 5, 'E': 2},
    'E': {'B': 4, 'C': 5, 'D': 2}
}

# Teste do algoritmo de Dijkstra
start_vertex = 'A'
distances, previous_nodes = dijkstra(graph, start_vertex)

# Exibição dos resultados
print(f"Distâncias mínimas a partir do vértice {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Distância até {vertex}: {distance}")

# Exibição dos caminhos mínimos
print(f"\nCaminhos mínimos a partir do vértice {start_vertex}:")
for vertex in graph:
    path = get_path(previous_nodes, start_vertex, vertex)
    print(f"Caminho até {vertex}: {' -> '.join(path)}")
