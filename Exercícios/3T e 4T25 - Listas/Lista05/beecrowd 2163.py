N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]

achou = False
x = y = 0

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if matriz[i][j] == 42:
            # Procurar os 8 vizinhos
            if (matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7 and
                matriz[i][j-1] == 7 and matriz[i][j+1] == 7 and
                matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7):
                x = i + 1
                y = j + 1
                achou = True
                break
    if achou:
        break

print(x, y)