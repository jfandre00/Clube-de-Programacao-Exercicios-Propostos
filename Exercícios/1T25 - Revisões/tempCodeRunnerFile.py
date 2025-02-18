import math

while True:
    try:
        # Lê o valor de N (nº original de postes)
        n = int(input())
        if n == 0:
            break

        # Lê estado de cada poste na cerca (0=danificado, 1=bom)
        cerca = input().split()

        # Cria array com posições dos postes bons
        bons = [i for i in range(n) if cerca[i] == '1']

        postes = 0
        if len(bons) == 0:
            postes += math.ceil(n / 2)
        else:
            for i in range(len(bons) - 1):
                # Calcula distância entre postes bons
                dist = bons[i+1] - bons[i]
                postes += (dist - 1) // 2
            dist = n - bons[-1] + bons[0]
            postes += (dist - 1) // 2

        # Imprime a saída
        print(postes)

    except EOFError:
        break