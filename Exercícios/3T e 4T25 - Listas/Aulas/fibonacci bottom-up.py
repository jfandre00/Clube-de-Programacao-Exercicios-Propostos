def fib(n):
    if n < 0:
        return None
    if n == 0:
        return 0

    # inicia com os 2 primeiros números da sequencia:
    penultimo = 0
    ultimo = 1
    # faz n - 1 iterações para calcular o n-ésimo termo:
    for i in range(n - 1):

        proximo = penultimo + ultimo
        penultimo, ultimo = ultimo, proximo

    return ultimo

fib_38 = fib(38)
print(fib_38)