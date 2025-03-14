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

while True:
    try:
        xa, ya, xb, yb = map(int, input().split())
        paredes = 0
        for i in range(xa - 1, xb):
            for j in range(ya - 1, yb):
                if grid[i][j] == '#':
                    paredes += 1
        largura = xb - xa + 1
        altura = yb - ya + 1
        resultado = reorganizar_paredes(largura, altura, paredes) % MOD
        print(resultado)
    except EOFError:
        break