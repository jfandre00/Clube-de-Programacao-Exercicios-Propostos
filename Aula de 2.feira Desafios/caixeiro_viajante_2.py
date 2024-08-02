#Code 2
from itertools import permutations
import math

# Função para calcular a distância entre duas cidades
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Função para calcular o comprimento total de um caminho
def total_distance(path, cities):
    total = 0
    for i in range(len(path) - 1):
        total += distance(cities[path[i]], cities[path[i + 1]])
    total += distance(cities[path[-1]], cities[path[0]])  # Voltar à cidade de origem
    return total

# Função para resolver o TSP usando força bruta
def tsp_bruteforce(cities):
    n = len(cities)
    shortest_path = None
    min_distance = float('inf')
    
    for path in permutations(range(n)):
        current_distance = total_distance(path, cities)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = path
    
    return shortest_path, min_distance


# Exemplo de uso
if __name__ == "__main__":
    # Cidades representadas por coordenadas (x, y)
    cities = [(0, 0), (1, 5), (5, 2), (3, 6)]
    
    # Resolver o TSP
    path, min_dist = tsp_bruteforce(cities)
    
    # Mostrar o resultado
    print("Caminho mais curto:", path)
    print("Distância total:", min_dist)




