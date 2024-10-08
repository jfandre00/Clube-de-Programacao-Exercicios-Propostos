'''def mount_marathon(n, cartas):
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
        
        if not movido:
            break  # Se nada foi movido, terminamos

    return len(pilhaDeCartas)

n = int(input()) 
cartas = list(map(int, input().split()))  

print(mount_marathon(n, cartas))'''

'''
Primeiro exemplo 
6 (cartas)
5 8 6 6 10 4 

podemos mover o 10 para a direita, para cima da carta 4

5 8 6 6 4
        10

mover o 8 para cima do 6

5  6  6  4
   8    10

nao consigo mais mover pois o 5 e 6 são menores que 8 e 10

------ tentando de outra forma

5 8 6 6 10 4

5 8 6 6  4
        10

5 8 6  4
    6  10

5 6  4
  6  10
  8

lógica - precisa ser maior ou igual e só move para a direita. Pilhas únicas são as que podem ser movidas
segredo é fazer da direita pra esquerda.
'''

'''
1. pilhas <- N
2. Para p de 1 até N-1:
   Se carta(p) >= carta(p+1):
    pilhas <- pilhas - 1
'''

def mount_marathon(n, cartas):
    pilhas = n

    for p in range(n-1):
        if cartas[p] >= cartas[p+1]:
            pilhas -= 1

    return pilhas

n = int(input()) 
cartas = list(map(int, input().split()))  

print(mount_marathon(n, cartas))





