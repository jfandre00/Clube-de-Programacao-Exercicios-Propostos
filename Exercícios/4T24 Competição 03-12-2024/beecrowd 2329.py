n = int(input())  
k = int(input())  
tamanhos = list(map(int, input().split()))  

# busca binária
inicio = 1
fim = max(tamanhos)
melhor_tamanho = 0

while inicio <= fim:
    meio = (inicio + fim) // 2
    total_fatias = 0

    for pao in tamanhos:
        total_fatias += pao // meio

    if total_fatias >= n:
        melhor_tamanho = meio  
        inicio = meio + 1  
    else:
        fim = meio - 1  

print(melhor_tamanho)