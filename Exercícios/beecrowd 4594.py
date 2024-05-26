n = int(input("Digite o valor de N: "))

# Leia a lista de N-1 números
lista = [int(x) for x in input("Digite os N-1 números separados por espaço: ").split()]

# Calcular a soma esperada de 1 a N usando a fórmula da soma dos primeiros N números naturais
soma_esperada = n * (n + 1) // 2

# Calcular a soma dos elementos fornecidos
soma_fornecida = sum(lista)

# A peça faltante é a diferença entre a soma esperada e a soma fornecida
peca_faltante = soma_esperada - soma_fornecida

# Imprimir a peça faltante
print(peca_faltante)