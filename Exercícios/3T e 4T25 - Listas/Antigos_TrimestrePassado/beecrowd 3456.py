#beecrowd 3456 - Divisibilidade por 7

#somar o dígito da unidade com 3 vezes o número que sobrou a esquerda
#assim reduzimos o número a outro e podemos aplicar o mesmo processo
#até que reste apenas um dígito. Se esse dígito for 7 ou 0 diginifica que ele é divisível por 7

#Exemplo 336 
#1. 33 x 3 + 6 = 105 (precisa ser divisível por 7)
#2. 10 x 3 + 5 = 35 (precisa ser divisível por 7)
#3. 3 x 3 + 5 = 14 (precisa ser divisível por 7)
#4. 1 x 3 + 4 = 7 (é divisível por 7)

# lê X
X = int(input().strip())

# enquanto tiver mais de um dígito, imprimimos e reduzimos
while X >= 10:
    print(X)
    X = (X // 10) * 3 + (X % 10)

# imprimimos o último (um dígito)
print(X)
