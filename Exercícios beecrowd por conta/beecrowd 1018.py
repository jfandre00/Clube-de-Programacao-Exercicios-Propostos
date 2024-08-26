def contarDinheiro(oDinheiro, aNota):
    qtdadeNotas = oDinheiro//aNota
    print(f'{qtdadeNotas} nota(s) de R$ {aNota},00')
    oDinheiro = oDinheiro - (qtdadeNotas*aNota)
    return oDinheiro

dinheiro = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(dinheiro)

for nota in notas:
    dinheiro = contarDinheiro(dinheiro, nota)

