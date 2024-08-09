import numpy as np

def nearest_neighbor_tsp(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    tour = [0]  # Começa na primeira cidade (índice 0)
    visited[0] = True

    current_city = 0

    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = float('inf')

        for city in range(num_cities):
            if not visited[city] and distance_matrix[current_city][city] < nearest_distance:
                nearest_distance = distance_matrix[current_city][city]
                nearest_city = city

        tour.append(nearest_city)
        visited[nearest_city] = True
        current_city = nearest_city

    tour.append(0)  # Retorna à cidade de origem
    return tour

# Exemplo de matriz de distâncias entre 5 cidades (A, B, C, D, E)
# As cidades são representadas por índices: 0, 1, 2, 3, 4
distance_matrix = np.array([
    [0, 2, 9, 10, 7],  # Distâncias da cidade A (índice 0) para outras cidades
    [2, 0, 6, 4, 3],   # Distâncias da cidade B (índice 1) para outras cidades
    [9, 6, 0, 8, 5],   # Distâncias da cidade C (índice 2) para outras cidades
    [10, 4, 8, 0, 1],  # Distâncias da cidade D (índice 3) para outras cidades
    [7, 3, 5, 1, 0]    # Distâncias da cidade E (índice 4) para outras cidades
])

tour = nearest_neighbor_tsp(distance_matrix)
print("Tour encontrado:", tour)
