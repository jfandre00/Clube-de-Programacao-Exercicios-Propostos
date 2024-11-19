#usar hash table, que permite busca em O(1), tempo constante

#1. Cria uma hash table associando valores do array com seus índices
#2. Para i de 0 até n-1, faz a busca do complemento do valor atual. Se encontrar, retorna os índices

#Entrada

array = [int(x) for x in input().strip("[]").split(",")]
alvo = int(input())

ht = {array[i]:i for i in range(len(array))}
for i in range(len(array) -1 ):
    j = ht.get(alvo - array[i], i)
    if j != i:
        break

#Saída
print(f"[{i}, {j}]")

