#Jogo Contando

# A pessoa mais a esquerda diz 1 em voz alta, a segunda pessoa diz 2 e assim por diante
# Quando chegar na pessoa n, a proxima vez vai para a pessoa n-1 e a contagem vai continuando
# Só que tem um detalhe: Se uma pessoa disser um número que é múltiplo de 7 ou que contém o dígito 7, a pessoa deve bater palmas ao invés de dizer o número. (representado por X)

# n -> número de pessoas
# m -> pessoa que estamos interessado em contar as palmas
# k -> número de vezes que a pessoa m bate palmas


# tenho 4 pessoas e quero saber quando a terceira pessoa bate 1 vez palmas

n, m, k = (int(x) for x in input().split())
while n !=0:
    num = 0
    palmas = 0
    pessoa = 1
    passo = 1
    while palmas < k:
        num += 1
        if pessoa == m and (num % 7 == 0 or '7' in str(num)):
            palmas += 1
        pessoa += passo
        if pessoa < 1:
            pessoa = 2
            passo = -passo
        elif pessoa > n:
            pessoa = n - 1
            passo = -passo  
    print(num)
    n, m, k = (int(x) for x in input().split())