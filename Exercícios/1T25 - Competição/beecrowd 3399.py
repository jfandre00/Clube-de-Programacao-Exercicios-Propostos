while True:
    try:
        # Leitura da entrada
        A, B, C, N = map(int, input().split())

        # Calculando a razão da sequência
        razão = B - A  # Ou C - B, pois é a mesma coisa

        # Calculando o enésimo termo da sequência
        resultado = A + (N - 1) * razão

        print(resultado)
    except EOFError:
        break
