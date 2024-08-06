def contar_postes_de_madeira(n, estados):
    distancia_poste = 2  # 2 metros
    comprimento_minimo_lacuna = 2  # pelo menos dois zeros para ser considerado, um zero só é descartado
    
    # Duplicar a lista p/ lidar com a circularidade
    estados_dobrados = estados + estados
    
    lacunas = []
    i = 0
    while i < len(estados): #percorrendo a lista fornecida no input, só passa para baixo se encontrar o 1
        if estados[i] == 1: #encontrando o numero 1, vai contar quantos zeros existem até o próximo 1
            j = i + 1  #achou o 1, pula para o próximo e verifica se é zero
            while j < len(estados_dobrados) and estados_dobrados[j] != 1: #para continuar percorrendo a lista dobrada 
                j += 1
            if j - i - 1 >= comprimento_minimo_lacuna: #para entrar na lista lacunas precisa ter mais do que 2 postes faltando
                lacunas.append(j - i - 1) #número de zero entre dois números 1
            i = j
        else: 
            i += 1

    quantidade = 0
    for lacuna in lacunas:
        quantidade += lacuna // distancia_poste #a quantidade de postes de madeira necessários é a parte inteira da divisao pela distância de cada poste 

    print(quantidade)

# Exemplo de uso

while True:
    n = int(input())
    if n == 0:
        break
    estados = list(map(int, input().split()))
    contar_postes_de_madeira(n, estados)