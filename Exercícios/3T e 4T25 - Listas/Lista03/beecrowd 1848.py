'''
Por exemplo a entrada *** representa o número 7, pois em binário 111 é igual a 7 em decimal.
Entrada --* representa o número 1, pois em binário 001 é igual a 1 em decimal.
Entrada *-- representa o número 4, pois em binário 100 é igual a 4 em decimal.

Temos 8 possibilidades de combinações de piscadas:
*** = 7
**- = 6
*-* = 5
*-- = 4
-** = 3
-* = 2
--* = 1
--- = 0
'''


contador = 0     # Soma das piscadas
gritos = 0       # Quantos "caw caw" já aconteceram

while True:
    entrada = input().strip()
    
    if entrada == "caw caw":   # Grito do corvo
        print(contador)
        contador = 0
        gritos += 1
        if gritos == 3:  # Só precisamos de 3 gritos
            break
    else:  # Piscada
        # Troca '*' por '1' e '-' por '0'
        binario = entrada.replace('*', '1').replace('-', '0')
        # Converte para inteiro base 2 e soma ao contador
        contador += int(binario, 2)


