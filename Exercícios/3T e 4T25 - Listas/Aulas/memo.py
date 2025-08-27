def fib(n, memo={}):
    if n < 0:
        return None
    
    # Casos base: fib(0) e fib(1)
    if n < 2:
        return n
    # Caso recursivo:
    # Se este subproblema ainda não foi resolvido,
    # calcula o resultado recursivamernte e o armazena.

    if n not in memo:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    # Retorna o resultado recuperado da hash table.
    return memo[n]

print(fib(38)) # Calcula o 38º termo da sequência de Fibonacci