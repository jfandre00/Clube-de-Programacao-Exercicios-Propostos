entrada = int(input())
lista = [int(x) for x in input().split()]


# Se o segundo for menor que o primeiro, a sequencia precisa ser sempre maior, menor, maior, menor e assim por diante
# Se o segundo for maior que o primeiro, a sequencia precisa ser sempre menor, maior, menor, maior e assim por diante
# caso não siga esse padrão, a resposta é 0 e o loop termina
# caso siga o padrão até o final, a resposta é 1

padrao = True
if len(lista) < 2:
    padrao = False
else:
    for i in range(1, len(lista)):
        if lista[i] == lista[i-1]:
            padrao = False
            break
    if padrao:
        for i in range(1, len(lista)-1):
            if not ((lista[i] > lista[i-1] and lista[i] > lista[i+1]) or (lista[i] < lista[i-1] and lista[i] < lista[i+1])):
                padrao = False
                break

if padrao:
    print(1)
else:
    print(0)
















