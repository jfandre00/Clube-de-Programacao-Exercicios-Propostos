#beecrowd 1839

#formas de re arranjar o retângulo n m com a quantidade de paredes dadas

#primeira linha da entrada informa as dimensões N e M da planta em unidades quadradas (numero de linhas e colunas do grid)
#As N linhas seguintes descrevem o grid de modo que unidades quadradas livres são representadas por . e paredes por #
#Cada uma das demais linhas da entrada é composta por 4 inteiros xa,ya,xb,yb que definem uma região através dos pontos (xa,ya) e (xb,yb)
#A entrada termina em fim de arquivo (EOF)

#Os pontos xa,ya e xb,yb definem uma região retangular no grid.
# xb - xa + 1 = largura
# yb - ya + 1 = altura

#o total de células no retângulo é a multiplicação da largura pela altura
#O que queremos descobrir é de quantas formas podemos reorganizar as paredes dentro do retângulo.

#Um exemplo temos um retângulo de 4 x 2 = 8 células
#Temos 3 paredes
#Análise combinatória: 8! / 3! * (8-3)! = 56
#Quantos subconjuntos de 3 elementos podemos formar com 8 elementos? O que eu uso? Combinação (fórmula): C(n,p) = n! / p! * (n-p)!
# Detalhe: As 56 combinações possíveis já incluem a combinação original, então para a resposta ser correta é necessário subtrair 1 -> C(n,p) - 1

#1. Calcular o total de células no retângulo: t = (xb - xa + 1) * (yb - ya + 1)

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
        resultado = reorganizar_paredes(largura, altura, paredes)
        print(resultado)
    except EOFError:
        break


