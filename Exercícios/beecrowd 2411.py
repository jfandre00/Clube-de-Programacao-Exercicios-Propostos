#beecrowd 2411

#1. Utilizamos um dicionário para mapear os movimentos possíveis do cavalo (dx, dy)
movimentos = { 
    1: (1,2),
    2: (2,1),
    3: (2,-1),
    4: (1, -2),
    5: (-1, -2),
    6: (-2, -1),
    7: (-2, 1),
    8: (-1, 2)
}

#Posições dos buracos - usamos uma lista de tuplas para armazenar as coordenadas das posições esburacadas.
buracos = [(1,3), (2,3), (2,5), (5,4)]

#Posição inicial do cavalo
x, y = 4, 3

#Lendo o número dos movimentos
N = int(input())
#Lendo os movimentos
M = list(map(int, input().split()))

#Simulando os movimentos - Iteramos sobre cada movimento na lista de movimentos fornecidos. Para cada movimento, atualizamos a posição (x,y) do cavalo de acordo com os deslocamentos (dx, dy). Incrementamos o contador de movimentos feitos. Se a nova posição (x,y) do cavalo for uma das posições dos buracos, interrompemos a simulação
movimentos_feitos = 0
for m in M:
    dx, dy = movimentos[m]
    x += dx
    y += dy
    movimentos_feitos += 1

    if (x, y) in buracos:
        break

#Imprimimos o número de movimentos feitos até o cavalo terminar o passeio ou cair em um buraco. Este código garante que o cavalo nunca saia do tabuleiro e que pare de se mover quando cai no buraco ou completa todos os movimentos fornecidos.

print(movimentos_feitos)