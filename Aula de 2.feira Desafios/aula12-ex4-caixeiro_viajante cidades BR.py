from itertools import permutations
import time

# Definição das tuplas de distâncias
distances = {
    ('SP', 'RJ'): 430,
    ('SP', 'BH'): 590,
    ('SP', 'Brasilia'): 1000,
    ('SP', 'Salvador'): 1960,
    ('RJ', 'BH'): 440,
    ('RJ', 'Brasilia'): 1160,
    ('RJ', 'Salvador'): 1650,
    ('BH', 'Brasilia'): 740,
    ('BH', 'Salvador'): 1380,
    ('Brasilia', 'Salvador'): 1450
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
nodes = ['SP', 'RJ', 'BH', 'Brasilia', 'Salvador']

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
    current_path = ('SP',) + perm + ('SP',)
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
