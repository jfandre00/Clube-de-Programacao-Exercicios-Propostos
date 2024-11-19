#Para um array de até 700 posições
#Complexidade O(n^2)


entrada = input().strip("[]").split(",")
entrada = [int(i) for i in entrada]
alvo = int(input())

#Vai comparar todos os elementos do array com todos os outros e se a soma for igual ao alvo, imprime os indices
for i in range(len(entrada)):
    for j in range(i + 1, len(entrada)):
        if entrada[i] + entrada[j] == alvo:
            print(f"[{i},{j}]")
            #Se encontrar uma solução, encerra o programa
            exit()