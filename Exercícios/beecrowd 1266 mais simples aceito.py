# Usando uma função p/ calcular o número de postes necessários
def calcular_postes(cerca):
    n = len(cerca)
    postes = 0

    #bons = [i for i in range(n) if cerca[i] == "1"] - solução usando list comprehension
    #lista para armazenar as posições dos postes
    bons = []

    # Vai buscar todos os índices possíveis na lista cerca
    for i in range(n):
    # Verifica se existe um poste na posição
        if cerca[i] == "1":
        # Se estiver presente, adiciona a posição i (index) à lista bons
            bons.append(i)

    if len(bons) > 0:
        # Calcula a distância entre postes existentes
        for i in range(len(bons) - 1):
            dist = bons[i + 1] - bons[i]
            postes += (dist - 1) // 2
        
        # Calcula a distância entre o último e o primeiro poste (cerca circular)
        dist = n - bons[-1] + bons[0]
        postes += (dist - 1) // 2
    else:
        # Se não há postes, coloca o mínimo necessário
        postes = (n + 1) // 2

    return postes

# Leitura da entrada e execução do cálculo
while True:
    n = int(input())
    if n <= 0:
        break
    cerca = input().split()
    resultado = calcular_postes(cerca)
    print(resultado)