#Solução para até 200.000 elementos
#complexidade O(nlogn)  

entrada = input().strip("[]").split(",")
entrada = [int(i) for i in entrada]
alvo = int(input())

# Tuplas com os índices junto com seus valores
entrada_com_indices = [(valor, i) for i, valor in enumerate(entrada)]

# Vamos ordernar os elementos pelo valor
entrada_com_indices.sort()

# Busca os dois números
for i in range(len(entrada_com_indices)):
    num1, idx1 = entrada_com_indices[i] #de tupla para variáveis
    complemento = alvo - num1 #quanto falta para dar o alvo

    # Busca binária pelo complemento
    esquerda, direita = i + 1, len(entrada_com_indices) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        num2, idx2 = entrada_com_indices[meio]
        if num2 == complemento:
            # Encontrou o complemento
            print(f"[{min(idx1, idx2)},{max(idx1, idx2)}]")
            exit()
        elif num2 < complemento:
            esquerda = meio + 1
        else:
            direita = meio - 1