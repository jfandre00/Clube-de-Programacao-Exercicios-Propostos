def busca_binaria(valor, array, inf=0):
    sup = len(array) - 1
    while inf <= sup:
        # Analisa o valor central entre inf e sup
        meio = (inf + sup) // 2
        valor_meio = array[meio][0]
        # Se for o valor buscado, retorna o índice
        if valor_meio == valor:
            return meio
        # Caso contrário, atualiza um dos limites
        if valor_meio < valor:
            inf = meio + 1
        else:
            sup = meio - 1
    # Retorna -1 se não encontrar o valor
    return -1

#Entrada

array = [int(x) for x in input().strip("[]").split(",")]
alvo = int(input())

array_ord = [(array[i], i) for i in range(len(array))]
array_ord.sort()
for i in range(len(array_ord) - 1):
    j = busca_binaria(alvo - array_ord[i][0], array_ord, i + 1)
    if j >= 0:
        break
i, j = sorted([array_ord[i][1], array_ord[j][1]])

#Saída
print(f"[{i},{j}]")