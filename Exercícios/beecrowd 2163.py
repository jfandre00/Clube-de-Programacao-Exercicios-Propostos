#Exercício beecrowd 2163

def acharSabre(matrix, n, m):
    for i in range(1, n-1):
        for j in range(1, m-1): #Não varre de 0 a n e 0 a m pois é se o 42 estiver nas bordas do terreno é impossível ter o sabre
            if (matrix[i][j] == 42 and
                matrix[i-1][j-1] == 7 and matrix[i-1][j] == 7 and matrix[i-1][j+1] == 7 and
                matrix[i][j-1] == 7 and matrix[i][j+1] == 7 and
                matrix[i+1][j-1] == 7 and matrix[i+1][j] == 7 and matrix[i+1][j+1] == 7): #Estamos testando todos os numeros em volta do 42 que foi encontrado
                return i+1, j+1  # Convertendo para coordenadas base 1
    return 0, 0

# Lendo a entrada
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)] #Fazendo lista de listas

x, y = acharSabre(matrix, n, m)
print(x, y)

'''if (matrix[i][j] == 42 and matrix[i-1][j-1] == matrix[i-1][j] == matrix[i-1][j+1] == matrix[i][j-1] == matrix[i][j+1] == matrix[i+1][j-1] == matrix[i+1][j] == matrix[i+1][j+1] == 7): 
    return i+1, j+1'''