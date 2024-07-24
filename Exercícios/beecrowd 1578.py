#beecrowd 1578
#O método .join() concatena elementos de uma lista em uma única string, separando esses elementos por um delimitador especificado, como um espaço por exemplo ou uma quebra de linha.

def formatacaoMatriz(matriz):
    # Calcula o comprimento máximo de cada coluna para formatação
    #Método: for dentro de for para percorrer todos os elementos, transformados em strings, descobrindo qual o mais comprido
    comprimentoColunas = [max(len(str(matriz[i][j])) for i in range(len(matriz))) for j in range(len(matriz))]

    
    linhasFormatadas = [] #será a matriz formatada
    for linha in matriz: #pega cada linha da matriz antes de formatar os espaços a esquerda
        linha_a_formatar = ' '.join(f'{valor:>{comprimentoColunas[j]}}' for j, valor in enumerate(linha))
        #dá um espaco de (valor) unidades e junta com a f string, alinhando a string direita (>)
        linhasFormatadas.append(linha_a_formatar) #cria a matriz com os mesmos numeros porem alinhados conforme os numeros maiores
    
    return '\n'.join(linhasFormatadas) #já retorna quebrando as linhas

x = 4

N = int(input())  # Número de matrizes

for _ in range(N): #uso _ pois é um contador simples
    M = int(input())  # Número de linhas e colunas da matriz
    matrizCompleta = [list(map(int, input().split())) for _ in range(M)]
    
    # Calcula o quadrado de cada elemento da matriz
    listaQuadrados = [[valor ** 2 for valor in linha] for linha in matrizCompleta]
    
    # Imprime o título da matriz
    print(f'Quadrado da matriz #{x}:')
    
    # Imprime a matriz formatada, chamando a função
    print(formatacaoMatriz(listaQuadrados))
    
    # Linha em branco entre as matrizes
    print()
    
    x += 1

############################### arrumar o esquema 


def formatacaoMatriz(matriz):
    # Calcula o comprimento máximo de cada coluna
    comprimentoColunas = [max(len(str(matriz[i][j])) for i in range(len(matriz))) for j in range(len(matriz))]

    linhasFormatadas = []
    for linha in matriz:
        # Formata cada valor para alinhar à direita
        linha_a_formatar = ' '.join(f'{valor:>{comprimentoColunas[j]}}' for j, valor in enumerate(linha))
        linhasFormatadas.append(linha_a_formatar)
    
    return '\n'.join(linhasFormatadas)

x = 4
N = int(input())  # Número de matrizes

for _ in range(N):
    M = int(input())  # Número de linhas e colunas da matriz
    matrizCompleta = [list(map(int, input().split())) for _ in range(M)]
    
    # Calcula o quadrado de cada elemento da matriz
    listaQuadrados = [[valor ** 2 for valor in linha] for linha in matrizCompleta]
    
    # Imprime o título da matriz
    print(f'Quadrado da matriz #{x}:')
    
    # Imprime a matriz formatada, chamando a função
    print(formatacaoMatriz(listaQuadrados))
    
    # Linha em branco entre as matrizes, mas não após a última
    if _ < N - 1:
        print()
    
    x += 1