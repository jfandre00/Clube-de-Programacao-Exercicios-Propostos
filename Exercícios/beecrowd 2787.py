L = int(input())
C = int(input())

# Determina a cor das casas na posição (L, C)
if (L % 2) == (C % 2):
    print(1)  # Mesma cor (branca)
else:
    print(0)  # Cores diferentes (preta)


'''Explicação do código para o problema do tabuleiro de xadrez
Entendimento do padrão de cores no tabuleiro de xadrez:

No tabuleiro de xadrez tradicional, a casa na linha 1, coluna 1 (canto superior esquerdo) é branca.
As cores das casas alternam-se entre branca e preta ao longo do tabuleiro.
Aplicação do código ao problema:

Entrada: São fornecidos dois valores, L (número de linhas) e C (número de colunas), que definem o tamanho do tabuleiro.
Cálculo da cor da casa no canto inferior direito:

l = int(input()) % 2: Calcula o resto da divisão de L por 2.
Se L for par, l será 0 (casa branca na linha L).
Se L for ímpar, l será 1 (casa preta na linha L).

c = int(input()) % 2: Calcula o resto da divisão de C por 2.
Se C for par, c será 0 (casa branca na coluna C).
Se C for ímpar, c será 1 (casa preta na coluna C).

Determinação da cor da casa no canto inferior direito:
A cor da casa no canto inferior direito será determinada pela comparação entre l e c.

print(int(l == c)): Imprime 1 se a cor for branca (ambos l e c são iguais), e 0 se a cor for preta (diferentes).
Exemplo de aplicação:
Se as entradas forem L = 6 e C = 9:

l = 6 % 2 = 0 (par, casa branca na linha 6)
c = 9 % 2 = 1 (ímpar, casa preta na coluna 9)
Nesse caso, l e c são diferentes, então a casa no canto inferior direito será preta, e o código imprimirá 0.

Esse método aproveita o padrão conhecido de cores do tabuleiro de xadrez (alternância entre branca e preta) e usa operações simples de módulo para determinar a cor da casa no canto inferior direito, independentemente das dimensões do tabuleiro fornecidas.'''