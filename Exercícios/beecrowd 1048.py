salario = float(input())
novo_salario = 0
p = 0

if salario <= 400:
    p = 15
elif salario <= 800:
    p = 12
elif salario <= 1200:
    p = 10
elif salario <= 2000:
    p = 7
else:
    p = 4

novo_salario = salario*(1+(p/100))

print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {(novo_salario-salario):.2f}\nEm percentual: {p} %')