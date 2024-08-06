def verificar_sudoku(matriz):
    listaTotal = []

    # Adiciona as linhas
    for i in range(9):
        listaTotal.append(matriz[i])
    
    # Verifica as colunas
    lista_vertical = []
    for l in range(9):
        coluna = [matriz[i][l] for i in range(9)]
        listaTotal.append(coluna)
    
    # Verifica os sub-quadrantes 3x3
    for range1 in range(0, 9, 3):
        for contador in range(0, 9, 3):
            sub_quadrante = []
            for i in range(range1, range1 + 3):
                for l in range(contador, contador + 3):
                    sub_quadrante.append(matriz[i][l])
            listaTotal.append(sub_quadrante)

    numeros_1_a_9 = set(range(1, 10))

    for sublista in listaTotal:
        if set(sublista) != numeros_1_a_9:
            return False
    
    return True

# Leitura de múltiplas instâncias
n = int(input())
instancias = []

for _ in range(n):
    matriz = []
    for _ in range(9):
        try:
            linha = list(map(int, input().split()))
        except EOFError:  #ficou dando esse erro no beecrowd, então fiz o tratamento.
            pass
        matriz.append(linha)
    instancias.append(matriz)

# Processamento e impressão dos resultados
for k, matriz in enumerate(instancias, start=1):
    if verificar_sudoku(matriz):
        print(f"Instancia {k}")
        print("SIM")
    else:
        print(f"Instancia {k}")
        print("NAO")
    print()