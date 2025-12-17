'''
Existem dois movimentos:

Vertical: Gastar 1 carga para explodir 1 torre inteira
Horizontal: Gastar 1 carga para cortar 1 andar de todas as torres

Para achar o custo mínimo, precisamos ordenar as torres da mais alta para a mais baixa

Depois, testar as combinações e ver qual é a que dá o menor custo.

Se não demolirmos nenhuma (0 vertical), o custo é 0 + a altura da 1ª (a mais alta).
Se demolirmos a 1ª mais alta (1 vertical), o custo é 1 + a altura da 2ª.
Se demolirmos as 2 mais altas (2 vertical), o custo é 2 + a altura da 3ª.
E assim por diante, até demolir todas (custo N).

O menor valor é a resposta.
'''

n = int(input())

alturas = list(map(int, input().split()))

alturas.sort(reverse=True)

# o pior custo possível é cortar todas as torres verticalmente
min_custo = n

for i in range(n):
    
    custo_atual = i + alturas[i]
    
    # atualiza o custo mínimo se encontrarmos um menor
    if custo_atual < min_custo:
        min_custo = custo_atual
        
print(min_custo)

