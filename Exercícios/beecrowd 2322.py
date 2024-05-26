n = int(input())
lista = [int(x) for x in input().split()]
lista.sort()
for i in range(len(lista)):
    if lista[i] != (i + 1):
        break
if lista[i] == (i + 1):
    i += 1
print(i + 1)

'''Versão melhorada
n = int(input())
lista = [int(x) for x in input().split()]

# Calcular a soma esperada de 1 a N
soma_esperada = n * (n + 1) // 2
# Calcular a soma dos elementos fornecidos
soma_fornecida = sum(lista)

# A peça faltante é a diferença entre a soma esperada e a soma fornecida
peca_faltante = soma_esperada - soma_fornecida

print(peca_faltante)
'''