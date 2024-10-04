def mount_marathon(n, cartas):
    pilhaDeCartas = cartas[:]  # Cópia da lista original

    while True:
        movido = False  # Para rastrear se algo foi movido
        i = 0
        
        # Itera pelas pilhas e tenta empilhar
        while i < len(pilhaDeCartas) - 1:
            if pilhaDeCartas[i] >= pilhaDeCartas[i + 1]:
                # Move a pilha atual para a pilha da direita
                pilhaDeCartas[i + 1] = pilhaDeCartas[i]
                # Remove a pilha atual
                pilhaDeCartas.pop(i)
                movido = True  # Indicamos que um movimento ocorreu
            else:
                i += 1  # Avança para a próxima pilha

        # Se nada foi movido, saímos do loop
        if not movido:
            break

    return len(pilhaDeCartas)  # Retorna o número de pilhas restantes

# Leitura da entrada
n = int(input())  # Número de cartas
cartas = list(map(int, input().split()))  # Lista com os valores das cartas

# Chama a função e imprime o resultado
print(mount_marathon(n, cartas))
