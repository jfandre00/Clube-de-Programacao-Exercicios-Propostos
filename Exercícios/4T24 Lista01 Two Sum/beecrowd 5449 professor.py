#Solução do professor Marcelo

#busca linear, percorrer o array inteiro, como ele não está ordenado, devemos percorrer o array inteiro

def busca_linear(valor, array, inicio=0):
    #Itera por cada elemento no array (a partir do índice "inicio")
    for i in range(inicio, len(array)):
        valor_array = array[i]
        if valor_array == valor:
            #Se for o valor procurado, retorna o índice
            return i
    #Retorna -1 se não encontrar o valor
    return -1

#Entrada
array = [int(x) for x in input().strip("[]").split(",")]
alvo = int(input())

for i in range(len(array) - 1):
    j = busca_linear(alvo - array[i], array, i + 1)
    if j >= 0:
        break

#Saída
print(f"[{i}, {j}]")