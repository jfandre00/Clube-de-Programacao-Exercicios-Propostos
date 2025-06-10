### arrumar tbm

'''
336 é divisível por 7:

33 * 3 + 6 = 105 -> precisa ser divisível por 7
10 * 3 + 5 = 35 -> precisa ser divisível por 7
3 * 3 + 5 = 14 -> precisa ser divisível por 7
1 * 3 + 4 = 7 -> precisa ser divisível por 7 
Acabamos em 7, então 336 é divisível por 7

############################

1764

176 * 3 + 4 = 532 -> é divisível por 7
53 * 3 + 2 = 161 -> é divisível por 7
16 * 3 + 1 = 49 -> é divisível por 7
4 * 3 + 9 = 21 -> é divisível por 7
2 * 3 + 1 = 7 -> é divisível por 7
''' 

numero = input()
resposta = None

while True:
    comprimento = len(numero)
    if len(numero) > 1:
        multiplicar = int(numero[0:comprimento-1])
        multiplicar *= 3
        multiplicar += int(numero[comprimento-1])
        print(multiplicar)
        resposta = multiplicar
        numero = str(resposta)
        if len(numero) == 1:
            break




