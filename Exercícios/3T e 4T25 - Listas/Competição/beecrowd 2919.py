import sys

# Lê TUDO de uma vez (muito mais rápido que input)
data = sys.stdin.buffer.read().split()
idx = 0  # ponteiro para percorrer os dados

# Enquanto ainda houver dados
while idx < len(data):
    # Quantidade de números do caso
    n = int(data[idx])
    idx += 1

    # Lista auxiliar:
    # lis[i] = menor valor possível para terminar
    # uma sequência crescente de tamanho i+1
    lis = []

    # Processa os n números do caso
    for _ in range(n):
        x = int(data[idx])
        idx += 1

        # Busca binária manual em lis
        # Queremos a primeira posição onde lis[pos] >= x
        left = 0
        right = len(lis)

        while left < right:
            mid = (left + right) // 2
            if lis[mid] < x:
                left = mid + 1
            else:
                right = mid

        # Se x é maior que todos, aumenta a sequência
        if left == len(lis):
            lis.append(x)
        else:
            # Senão, troca para terminar com um valor menor
            # Isso NÃO muda o tamanho, só melhora futuras chances
            lis[left] = x

    # O tamanho da lis é a resposta do caso
    print(len(lis))
