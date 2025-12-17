# Lê o número de alunos
N = int(input().strip())

# Lê a lista de notas
notas = list(map(int, input().split()))

# Dicionário para contar quantas vezes cada nota aparece
frequencia = {}

for nota in notas:
    if nota in frequencia:
        frequencia[nota] += 1
    else:
        frequencia[nota] = 1

# Descobre a maior frequência entre as notas
maior_freq = max(frequencia.values())

# Inicializa a variável que vai guardar a maior nota com maior frequência
resultado = -1  # valor inicial baixo, menor que qualquer nota possível

# Percorre todas as notas e suas frequências
for nota, freq in frequencia.items():
    if freq == maior_freq:
        if nota > resultado:
            resultado = nota

# Imprime a nota mais frequente (se houver empate, imprime a maior)
print(resultado)