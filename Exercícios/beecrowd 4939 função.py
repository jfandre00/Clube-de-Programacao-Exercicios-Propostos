def verificar_pontos(carta, valor, pontosA, pontosB):
    if carta + valor < quantidadeCartas and all(lista[carta + i] not in ALTAS for i in range(1, valor + 1)):    
    #o all simplificou a minha primeira versão e faz as verificações das cartas que vem depois que High Card que o Player virou, conforme as regras do jogo (A=4 / K=3 / Q=2 / J=1)
    #carta + valor < quantidadeCartas para ter certeza que a verificação não vai cair fora da lista
        if carta % 2 == 0: #como é o A que começa sempre que for par será A (0,2,4,6...)
            print(f'Player A scores {valor} point(s).')
            pontosA += valor
        else:
            print(f'Player B scores {valor} point(s).')
            pontosB += valor
    return pontosA, pontosB 
    #retornei os pontosA e pontosB para eles não se perderem dentro da função e poderem ser acumulados.

ALTAS = ['jack', 'queen', 'king', 'ace']
pontosA = 0
pontosB = 0
lista = []
quantidadeCartas = 52

for entrada in range(quantidadeCartas):
    lista.append(input())  #colocando as entradas na lista

for carta in range(quantidadeCartas):
    if lista[carta] in ALTAS:
        valor = ALTAS.index(lista[carta]) + 1  
        #Se lista[carta] for 'jack', ALTAS.index('jack') retorna 0 e assim por diante
        pontosA, pontosB = verificar_pontos(carta, valor, pontosA, pontosB)

print(f'Player A: {pontosA} point(s).')
print(f'Player B: {pontosB} point(s).')