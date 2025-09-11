n = int(input())
for i in range(1, n*4, 4): # range(inicio, fim, passo)
    print(i, i+1, i+2, "PUM") # imprime a sequência de números seguida de "PUM"

# o i vai começar valendo 1 e vai até n*4, com passo 4
# passo 4 significa que a cada iteração o valor de i aumenta em 4
# na primeira iteração i vale 1, na segunda iteração i vale 5, na terceira iteração i vale 9, e assim por diante...