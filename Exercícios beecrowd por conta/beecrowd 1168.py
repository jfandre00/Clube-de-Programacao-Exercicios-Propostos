lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_quantidade_leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


quantidade = int(input())


for i in range(quantidade):
    lista = []
    n = str(input())
    for i in range(len(n)):
        lista.append(n[i])

    total = 0
    for i in range(len(lista)):
        total += lista_quantidade_leds[lista_numeros.index(int(lista[i]))]

    print(f'{total} leds')





          