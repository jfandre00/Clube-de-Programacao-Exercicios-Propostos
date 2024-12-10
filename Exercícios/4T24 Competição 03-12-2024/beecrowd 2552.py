#Tentando resolver após a competição

# entrada n, m separados por espaço
# proximas n linhas com m elementos separados por espaço
# entrada termina com EOF

# para resolver: vamos adicionar uma linha de zeros ao redor da matriz
# e vamos percorrer a matriz, se o elemento for 1, o retorno é 9
# se o elemento for 0, vamos contar quantos 1s tem ao redor dele

# 1 - função adicionar os zeros ao redor da matriz
def adicionar_zeros(matrix):
    n = len(matrix)  # número de linhas
    m = len(matrix[0])  # número de colunas
    matrix = [[0 for j in range(m+2)]] + matrix + [[0 for j in range(m+2)]]  # adicionar uma linha de zeros no início e no final
    for i in range(1, n+1):
        matrix[i] = [0] + matrix[i] + [0]  # adicionar um zero no início e no final de cada linha
    return matrix

# função para contar os 1s ao redor de um elemento (não contar as diagonais)

def count_ones(matrix, i, j):
    count = 0
    if matrix[i-1][j] == 1:
        count += 1  # se o elemento acima for 1, incrementa o contador
    if matrix[i+1][j] == 1:
        count += 1  # se o elemento abaixo for 1, incrementa o contador
    if matrix[i][j-1] == 1:
        count += 1  # se o elemento à esquerda for 1, incrementa o contador
    if matrix[i][j+1] == 1:
        count += 1  # se o elemento à direita for 1, incrementa o contador
    return count

'''
#testes
print('Começando os testes')
n, m = 4, 4
matrix = [[0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]
matrix = adicionar_zeros(matrix)
print(matrix)
for i in range(1, n+1):
    for j in range(1, m+1):
        if matrix[i][j] == 1:
            print(9, end='')
        else:
            print(count_ones(matrix, i, j), end='')
    print()

print('Fim dos testes')
'''

# Loop para ler as entradas e chamar as funções

while True:
    try:
        n, m = map(int, input().split())
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, input().split())))
        matrix = adicionar_zeros(matrix)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if matrix[i][j] == 1: # 2. se o elemento for 1, imprime 9
                    print(9, end='')
                else:
                    print(count_ones(matrix, i, j), end='')
            print()
    except EOFError:
        break
