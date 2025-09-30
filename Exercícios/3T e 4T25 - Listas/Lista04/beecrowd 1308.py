entradas = int(input())

# Removi o while True pois estava dando time limit exceeded
# O loop agora roda exatamente o número de vezes indicado na entrada

for _ in range(entradas):
    guerreiros = int(input())
    baixo, alto = 1, guerreiros
    resposta = 0
    while baixo <= alto: # Busca binária para encontrar o maior n
        meio = (baixo + alto) // 2 # Pega o meio do intervalo atual
        if meio * (meio + 1) // 2 <= guerreiros: # Verifica se a soma dos n primeiros números naturais é menor ou igual ao número de guerreiros
            resposta = meio
            baixo = meio + 1
        else:
            alto = meio - 1
    print(resposta)