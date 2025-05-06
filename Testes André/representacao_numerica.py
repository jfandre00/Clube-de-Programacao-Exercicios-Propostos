#Representação Numérica

#Representação numérica é a forma como os números são representados em um computador. Existem várias formas de representação numérica, mas as mais comuns são a representação binária, decimal e hexadecimal.

print(0.1 + 0.2)    # 0.30000000000000004
# Isso acontece porque os números em ponto flutuante são representados em binário, e nem todos os números decimais podem ser representados exatamente em binário.

from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)        # 0.3




