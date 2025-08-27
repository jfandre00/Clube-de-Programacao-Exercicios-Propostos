# Função recursiva para calcular o imposto

def calcular_imposto_rec(salario):
    if salario <= 2000:
        return 0.0
    elif salario <= 3000:
        return (salario - 2000) * 0.08
    elif salario <= 4500:
        return (salario - 3000) * 0.18 + calcular_imposto_rec(3000)
    else:
        return (salario - 4500) * 0.28 + calcular_imposto_rec(4500)

salario = float(input())
imposto = calcular_imposto_rec(salario)

print(f"R$ {imposto:.2f}" if imposto > 0 else "Isento")
