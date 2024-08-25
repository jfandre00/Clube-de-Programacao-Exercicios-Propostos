'''
def nenhuma_alta(lista):
 for carta in lista:
    if carta in ALTAS:
        return False
    else:
        return True
'''

'''Recebi runtime error do beecrowd e percebi que eu não estava respeitando os limites da lista para
fazer as verificações. Resolvi colocando verificações carta + 1 < 52, carta + 2 < 52, etc., para garantir que ele nem teste caso esteja no final da lista.'''

ALTAS = ('jack', 'queen', 'king', 'ace')
pontosA = 0
pontosB = 0
lista = []
#para testar sem fazer a lista pegue o teste depois do código! ou use a lista pronta abaixo

'''lista = ['three', 'seven','queen','eight','five','ten','king','eight','jack','queen','six','queen','jack','eight','seven','three','ten','four','king','nine','six','seven','ace','four','jack','ace','ten','nine','ten','queen','ace','king','seven','two','five','two','five','nine','three','king','six','eight','jack','six','five','four','two','ace','four','three','two','nine']'''

for entrada in range(52):
    lista.append(input()) #peguei todas as entradas e coloquei na lista

#Para resolver não usei funções, mas fiz um código que funcionou para verificar uma ocorrência e depois fui mudando os pontos e as regras de verificação.
# Vou fazer uma nova versão tentando implementar funções     

for carta in range(52): #rodando todas as cartas
    if lista[carta] in ALTAS: #achei um High Card
        if lista[carta] == 'jack':  #testei se é JACK
            if carta + 1 < 52 and lista[carta + 1] not in ALTAS: #verificando as cartas seguintes e o final da lista, e também se a próxima carta não é uma High Card
                ponto = 1
                if carta % 2 == 0:
                    print(f'Player A scores {ponto} point(s).')
                    pontosA += ponto
                else:
                    print(f'Player B scores {ponto} point(s).')
                    pontosB += ponto

        elif lista[carta] == 'queen': #testei se é QUEEN
            if carta + 2 < 52 and lista[carta + 1] not in ALTAS and lista[carta + 2] not in ALTAS: #verificando as cartas seguintes e o final da lista, e também se a próxima carta não é uma High Card
                ponto = 2
                if carta % 2 == 0:
                    print(f'Player A scores {ponto} point(s).')
                    pontosA += ponto
                else:
                    print(f'Player B scores {ponto} point(s).')
                    pontosB += ponto

        elif lista[carta] == 'king':
            if carta + 3 < 52 and lista[carta + 1] not in ALTAS and lista[carta + 2] not in ALTAS and lista[carta + 3] not in ALTAS: #verificando as cartas seguintes e o final da lista, e também se a próxima carta não é uma High Card
                ponto = 3
                if carta % 2 == 0:
                    print(f'Player A scores {ponto} point(s).')
                    pontosA += ponto
                else:
                    print(f'Player B scores {ponto} point(s).')
                    pontosB += ponto

        elif lista[carta] == 'ace':
            if carta + 4 < 52 and lista[carta + 1] not in ALTAS and lista[carta + 2] not in ALTAS and lista[carta + 3] not in ALTAS and lista[carta + 4] not in ALTAS: #verificando as cartas seguintes e o final da lista, e também se a próxima carta não é uma High Card
                ponto = 4
                if carta % 2 == 0:
                    print(f'Player A scores {ponto} point(s).')
                    pontosA += ponto
                else:
                    print(f'Player B scores {ponto} point(s).')
                    pontosB += ponto
    
print(f'Player A: {pontosA} point(s).')
print(f'Player B: {pontosB} point(s).')

'''
three
seven
queen
eight
five
ten
king
eight
jack
queen
six
queen
jack
eight
seven
three
ten
four
king
nine
six
seven
ace
four
jack
ace
ten
nine
ten
queen
ace
king
seven
two
five
two
five
nine
three
king
six
eight
jack
six
five
four
two
ace
four
three
two
nine
'''
