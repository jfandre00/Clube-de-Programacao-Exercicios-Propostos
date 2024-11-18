#Solução para até 700.000 elementos
#complexidade O(n)

entrada = input().strip("[]").split(",")
entrada = [int(i) for i in entrada]
alvo = int(input())

# Dicionário para armazenar valores e seus índices
complementos = {}

for i, numero in enumerate(entrada):
    complemento = alvo - numero #quanto falta para dar o alvo
    if complemento in complementos:
        # Encontramos o par, imprime os índices
        print(f"[{complementos[complemento]},{i}]")
        exit()  # Termina o programa
    # Armazena o índice do número atual no dicionário
    complementos[numero] = i