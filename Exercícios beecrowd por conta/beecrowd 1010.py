linha1 = input().strip()
linha2 = input().strip()

valores1 = linha1.split()
valores2 = linha2.split()

codigo1 = int(valores1[0])
pecas1 = int(valores1[1])
valor1 = float(valores1[2])

codigo2 = int(valores2[0])
pecas2 = int(valores2[1])
valor2 = float(valores2[2])

valor_a_pagar = (pecas1*valor1) + (pecas2*valor2)

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')
