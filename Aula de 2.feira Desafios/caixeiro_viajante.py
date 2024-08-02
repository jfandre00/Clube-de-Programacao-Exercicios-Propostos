from itertools import permutations
import time

# Definição das tuplas de distâncias
distances = {
    ('A', 'B'): 1,
    ('A', 'C'): 1,
    ('B', 'E'): 8,
    ('B', 'C'): 9,
    ('C', 'D'): 7,
    ('D', 'E'): 1,
    ('B', 'D'): 2,
    ('E', 'C'): 1
}

# Função para calcular a distância total de uma permutação
def calculate_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        if (path[i], path[i+1]) in distances:
            total_distance += distances[(path[i], path[i+1])]
        elif (path[i+1], path[i]) in distances:
            total_distance += distances[(path[i+1], path[i])]
        else:
            return float('inf')  # Caminho inválido
    return total_distance

# Nós
nodes = ['A', 'B', 'C', 'D', 'E']

# Geração de todas as permutações possíveis (fixando o nó inicial 'A')
permutations_list = list(permutations(nodes[1:]))  # Permutações dos nós exceto 'A'

# Variáveis para armazenar a menor distância e o melhor caminho
min_distance = float('inf')
best_path = None

# Contador de operações
operation_count = 0

# Tempo de início
start_time = time.time()


# Avaliação de todas as permutações
for perm in permutations_list:
    current_path = ('A',) + perm + ('A',)
    current_distance = calculate_distance(current_path, distances)
    operation_count += 1  # Contar a operação de cálculo da distância
    if current_distance < min_distance:
        min_distance = current_distance
        best_path = current_path

# Tempo de fim
end_time = time.time()

# Exibição da melhor rota, distância total e contagem de operações
print("Melhor Rota:", " -> ".join(best_path))
print("Distância Total:", min_distance)
print("Número de Operações:", operation_count)
print("Tempo Total:", end_time - start_time, "segundos")
