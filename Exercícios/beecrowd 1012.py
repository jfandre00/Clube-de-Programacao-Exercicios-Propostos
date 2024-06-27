# Leitura dos valores de entrada
A, B, C = map(float, input("Digite os valores de A, B e C, separados por espaço: ").split())

# a) Área do triângulo retângulo
area_triangulo = (A * C) / 2

# b) Área do círculo (usando pi = 3.14159)
pi = 3.14159
area_circulo = pi * C**2

# c) Área do trapézio
area_trapezio = ((A + B) * C) / 2

# d) Área do quadrado
area_quadrado = B**2

# e) Área do retângulo
area_retangulo = A * B

# Exibindo os resultados
print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")