#beecrowd 5078

'''
1. Problema: Vasiliy quer saber em quantas lojas ele pode comprar sua bebida favorita em diferentes dias, dado o quanto ele pode gastar em cada dia.
Entradas: Número de lojas n. / Lista de preços das lojas x. / Número de dias q. /Lista de valores que ele pode gastar em cada dia m.
Saída: Para cada dia, o número de lojas onde ele pode comprar a bebida.
2. Abordagem tradicional que gerou time limit exceeded: Para cada valor em m, iterar sobre todos os preços em x e contar quantos são menores ou iguais ao valor atual.
Complexidade: O(n * q), onde n é o número de lojas e q é o número de dias. Isso pode ser ineficiente para grandes valores de n e q.
3. Melhorando a Eficiência com Busca Binária
Ordenação: Ordenar a lista de preços x uma vez. A ordenação tem complexidade O(n log n).
Busca Binária: Para cada valor em m, usar busca binária para encontrar quantos preços em x são menores ou iguais ao valor atual. A busca binária tem complexidade O(log n).
4. Por que Busca Binária?
Eficiência: A busca binária é eficiente para encontrar elementos em uma lista ordenada. Em vez de iterar sobre todos os elementos, ela divide a lista em metades, reduzindo o número de comparações.
Complexidade Reduzida: Com a busca binária, a complexidade total da solução se torna O(n log n + q log n), que é muito mais eficiente do que O(n * q).
5. Implementação
Ordenação da Lista: Ordenar a lista de preços x.
Busca Binária Manual: Implementar a busca binária para encontrar o número de lojas onde o preço é menor ou igual ao valor que Vasiliy pode gastar.
'''

# Função para realizar a busca binária (inspirado no exercício que o professor da aula do Professor Vitor passou)
def busca_binaria(arr, valor):
    esquerda, direita = 0, len(arr)
    while esquerda < direita:
        meio = (esquerda + direita) // 2
        if arr[meio] <= valor:
            esquerda = meio + 1
        else:
            direita = meio
    return esquerda


n = int(input())  # numero de lojas
x = list(map(int, input().split()))  # precos das n lojas
q = int(input())  # total de dias

# Ordenar a lista de preços das lojas
x.sort()

# Para cada dia, calcular o número de lojas e imprimir o resultado
for _ in range(q):
    m = int(input())  # quanto que pode gastar no dia, por q dias
    # Chamando a função busca binária para encontrar o número de lojas
    contador = busca_binaria(x, m)
    print(contador)

