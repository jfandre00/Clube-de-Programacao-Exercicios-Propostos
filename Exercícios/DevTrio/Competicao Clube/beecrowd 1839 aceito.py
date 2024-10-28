def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def combinacao(n, p):
    if p > n:
        return 0
    return fatorial(n) // (fatorial(p) * fatorial(n - p))

def reorganizar_paredes(largura, altura, paredes):
    total_celulas = largura * altura
    combinacoes = combinacao(total_celulas, paredes)
    return combinacoes - 1
    
# Leitura da entrada
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

MOD = 10**9 + 7

# Pré-processamento: criar uma matriz de prefixo para contar as paredes
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = (grid[i-1][j-1] == '#') + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

while True:
    try:
        xa, ya, xb, yb = map(int, input().split())
        # Calcular o número de paredes na submatriz usando a matriz de prefixo
        paredes = (prefix_sum[xb][yb] - prefix_sum[xa-1][yb] - prefix_sum[xb][ya-1] + prefix_sum[xa-1][ya-1])
        largura = xb - xa + 1
        altura = yb - ya + 1
        resultado = reorganizar_paredes(largura, altura, paredes) % MOD
        print(resultado)
    except EOFError:
        break