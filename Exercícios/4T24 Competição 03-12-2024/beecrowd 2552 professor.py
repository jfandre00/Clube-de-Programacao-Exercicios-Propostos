# N = 4 M = 4
# 0 0 1 1
# 0 1 0 1
# 0 0 1 0
# 1 1 0 1
# aonde tem 1 imprime 9
# aonde tem 0 imprime a quantidade de 1s ao redor (não contar as diagonais)
# Resposta será:
# 0 2 9 9
# 1 9 4 9
# 1 3 9 3
# 9 9 3 9

#1. Cria uma matriz N x M com valor 9 nas células onde há pão de queijo e 0 nas demais
#2. Para cada célula da matriz
# Se o valor for 0 : conta o n. de valores 9 ao redor da célula e imprime o resultado
# precisa tomar cuidado com as bordas da matriz
# Se o valor for 9 : imprime 9
 
while True:
    try:
        n, m = (int(x) for x in input().split())
    
        # Cria uma matriz com valor 9 nas células onde há pão de queijo e 0 nas demais
        matriz = []
        for _ in range(n):
            matriz.append([9 if x == '1' else 0 for x in input().split()])

        # Percorre cada célula [i,j] da matriz
        for i in range(n):
            for j in range(m):
                # Se o valor for 0, soma o n. de valores 9 ao redor da célula
                if matriz[i][j] == 0:

                    # Se não está na borda superior, verifica a célula acima
                    if i > 0 and matriz[i-1][j] == 9:
                        matriz[i][j] += 1
                    
                    # Se não está na borda inferior, verifica a célula abaixo
                    if i < n-1 and matriz[i+1][j] == 9:
                        matriz[i][j] += 1
                    
                    # Se não está na borda esquerda, verifica a célula à esquerda
                    if j > 0 and matriz[i][j-1] == 9:
                        matriz[i][j] += 1

                    # Se não está na borda direita, verifica a célula à direita
                    if j < m-1 and matriz[i][j+1] == 9:
                        matriz[i][j] += 1

                print(matriz[i][j], end='') # Imprime o valor da célula
                    
            # Ao fim de cada linha, imprime uma quebra de linha
            print()

    except EOFError:
        break

#Complexidade O(n*m) para percorrer a matriz


