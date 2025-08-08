caso = 1
primeiro_caso = True

while True:
    try:
        n = int(input())  # número desejado
        entrada = list(map(str, input().split()))  # pares de dados
        F = 0
        M = 0

        for i in range(0, len(entrada), 2):
            tamanho = int(entrada[i])
            mOuF = entrada[i+1]
            if tamanho == n:
                if mOuF == "F":
                    F += 1
                else:
                    M += 1

        paresIguais = F + M

        if not primeiro_caso:
            print()  # linha em branco antes do próximo caso
        primeiro_caso = False

        print(f"Caso {caso}:")
        print(f"Pares Iguais: {paresIguais}")
        print(f"F: {F}")
        print(f"M: {M}")

        caso += 1

    except EOFError:
        break
