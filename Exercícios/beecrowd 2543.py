'''
A entrada contém vários casos de teste. A primeira linha de cada caso contém dois inteiros N e I (1 ≤ N ≤ 104, 1000 ≤ I ≤ 9999), o número de gameplays publicados na página e o seu identificador na universidade, respectivamente.

As próximas N linhas descrevem os gameplays publicados. Cada gameplay é descrito por dois inteiros i e j (1000 ≤ i ≤ 9999, j=0 ou 1), onde i é o identificador na universidade do autor do gameplay, e j=0 se o gameplay é de Contra-Strike, ou j=1 se é de Liga of Legendas.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma única linha com um número indicando quantos gameplays seus de Contra-Strike foram publicados na página.
'''
try:
    while True:
        entrada = input().strip()
        if not entrada:
            break
        N, I = map(int, entrada.split())

        count = 0
        for index in range(N):  
            id_jogador, jogo = map(int, input().strip().split())
            if id_jogador == I and jogo == 0:
                count += 1

        print(count)
except EOFError:
    pass