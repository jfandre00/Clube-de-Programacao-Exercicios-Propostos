def euclidean_gcd(a, b):
    """
    Calcula o Máximo Divisor Comum (MDC) de 
   dois números inteiros usando o Algoritmo de Euclides.
    
    Parâmetros:
    a (int): Primeiro número inteiro.
    b (int): Segundo número inteiro.
    
    Retorna:
    int: O Máximo Divisor Comum (MDC) de a e b.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Exemplo de uso
num1 = 144
num2 = 96

# Calcula o MDC
mdc = euclidean_gcd(num1, num2)

# Imprime o resultado
print(f"O Máximo Divisor Comum (MDC) de {num1} e {num2} é {mdc}.")


