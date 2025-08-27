'''Solução simples e correta: contar quantos trechos consecutivos de diferença constante existem. Se N==1 a resposta é 1. Para N>=2, calcule as diferenças consecutivas d[i] = a[i+1]-a[i] e conte quantos blocos consecutivos de valores iguais existem em d. Cada bloco corresponde a uma escadinha máxima.'''

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

count = 1  # pelo menos uma escadinha garantida
prev = a[1] - a[0] # diferença entre os dois primeiros elementos - estamos tratando como uma progressão aritmética

for i in range(1, n - 1):
    cur = a[i + 1] - a[i] # diferença entre o elemento atual e o próximo
    if cur != prev: # se a diferença mudou, significa que a escadinha terminou
        count += 1 # incrementa o contador de escadinhas
        prev = cur # atualiza a diferença para a próxima iteração

print(count)
