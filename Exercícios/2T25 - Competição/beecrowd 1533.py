#lista com N inteiros, representando o quanto cada pessoa é suspeita
#decidir que é o assassino de acordo com o método citado

while True:
    N = int(input()) #suspeitos
    if N == 0: #se N for 0, encerra o programa
        break
    suspeitos = list(map(int, input().split())) #lista com N inteiros, represent o qto cada pessoa é suspeita

    #criar um uma tupla contendo o índice e o valor de cada suspeito
    suspeitos_com_indice = [(i, suspeitos[i]) for i in range(N)]

    #ordenar a lista de suspeitos pela quantidade de suspeita
    suspeitos_com_indice.sort(key=lambda x: x[1], reverse=True)

    # pegar o segundo suspeito mais suspeito
    if N == 1:
        print(suspeitos_com_indice[0][0] + 1)  # Se só há um suspeito, ele é o assassino
    else:
        print(suspeitos_com_indice[1][0] + 1)  # O segundo mais suspeito é o assassino
    

    