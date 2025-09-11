valor = int(input())
print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in range(len(notas)):
    quantidade = valor // notas[nota]
    valor = valor % notas[nota] # Resto da divisão
    print(f"{quantidade} nota(s) de R$ {notas[nota]},00")
