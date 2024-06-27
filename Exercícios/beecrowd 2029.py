# Valor de pi
pi = 3.14

while True:
    try:
        # Leitura do volume V
        V = float(input())

        # Leitura do diâmetro D
        D = float(input())

        # Calcula o raio
        R = D / 2

        # Calcula a área da boca do recipiente
        A = pi * (R ** 2)

        # Calcula a altura do recipiente
        H = V / A

        # Imprime os resultados formatados
        print(f"ALTURA = {H:.2f}")
        print(f"AREA = {A:.2f}")

    except EOFError:
        break