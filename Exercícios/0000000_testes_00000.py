def verificar_sudoku(matriz):
    listaTotal = []

    for i in range(9):
        listaTotal.append(matriz[i])
    
    # Verificação das linhas
    for linha in listaTotal:
        if set(linha) != set(range(1, 10)):
            return False
    
    # Verificação das colunas
    for l in range(9):
        coluna = {listaTotal[i][l] for i in range(9)}
        if coluna != set(range(1, 10)):
            return False

    # Verificação dos sub-quadrantes 3x3
    for range1 in range(0, 9, 3):
        for contador in range(0, 9, 3):
            sub_quadrante = {listaTotal[i][l] for i in range(range1, range1 + 3) for l in range(contador, contador + 3)}
            if sub_quadrante != set(range(1, 10)):
                return False

    return True

# Leitura de múltiplas instâncias
n = int(input())
instancias = []

# Leitura de todas as instâncias
for _ in range(n):
    matriz = []
    for _ in range(9):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    instancias.append(matriz)
    if _ < n - 1:
        input()  # Ler linha em branco entre instâncias

# Processamento e impressão dos resultados
for k, matriz in enumerate(instancias, start=1):
    if verificar_sudoku(matriz):
        print(f"Instancia {k}")
        print("SIM")
    else:
        print(f"Instancia {k}")
        print("NAO")
    print()