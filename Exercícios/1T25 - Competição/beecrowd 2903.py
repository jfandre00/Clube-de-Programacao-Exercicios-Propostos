# bob gosta de tudo simétrico, sua casa, suas roupas, seu carro e sua comida e pizza não poderia ser diferente
# todos os toppings da pizza que ele come precisam ser simétricos, ou seja, se ele come uma pizza com pepperoni, ele precisa comer uma pizza com pepperoni do outro lado, se ele come uma pizza com cogumelos, ele precisa comer uma pizza com cogumelos do outro lado, e assim por diante.

'''
Entrada
The input consists of a single line that contains a rational number R (0 < R < 360) indicating the angle of the rotational symmetry demonstration. This number has exactly two digits after the decimal point.

Saída
Output a single line with an integer representing the maximum amount of equal slices Bob can cut the pizza in, based on the provided information'
'''
'''
Leitura do Ângulo R: O ângulo R é lido como um número de ponto flutuante e convertido para um inteiro multiplicando por 100 (para evitar problemas com aritmética de ponto flutuante).

Cálculo do GCD: Calculamos o máximo divisor comum (GCD) entre 36000 (360 * 100) e o valor inteiro de R (R_int). Isso nos ajuda a determinar a maior simetria possível.

Determinação do Número de Fatias: O número máximo de fatias N é obtido dividindo 36000 pelo GCD calculado. Isso funciona porque N deve ser tal que 360° dividido por N resulte no ângulo de simetria R, ou um submúltiplo dele.

Saída do Resultado: O valor de N é impresso, representando o número máximo de fatias iguais em que a pizza pode ser cortada mantendo a simetria rotacional de R graus.

Por exemplo, se R é 45.00, R_int é 4500. O GCD entre 36000 e 4500 é 4500. Então, N = 36000 / 4500 = 8, que é a resposta correta. Essa abordagem garante que encontramos o maior número de fatias possível que mantém a simetria desejada.'
'''

import math

R = float(input())
R_convertido_inteiro = int(round(R * 100))

#utilizando a função math.gcd para encontrar o máximo divisor comum entre 36000 e R_convertido_inteiro

max_divisor = math.gcd(36000, R_convertido_inteiro)
N = 36000 // max_divisor

print(N)