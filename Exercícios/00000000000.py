while True:
    try:
        contador = 0
        valores_fora_do_intervalo = [] 
        numeros = list(map(int, input().split()))

        numeros.insert(12, 0)  # Adiciona um valor que não é preenchido em linha 3 - "N"

        B = []
        I = []
        N = []
        G = []
        O = []

        for i in range(0, 21, 5):
            B.append(numeros[i])
            I.append(numeros[i+1])
            N.append(numeros[i+2])
            G.append(numeros[i+3])
            O.append(numeros[i+4])

        N.remove(0)  # Remove o 0 já que os números estão corretamente separados agora

        intervalos = {
            'B': (1, 15),
            'I': (16, 30),
            'N': (31, 45),
            'G': (46, 60),
            'O': (61, 75) }  # Intervalos para cada coluna

        # Verifica se todos os elementos estão no intervalo do dicionário acima
        todos_intervalos_ok = True
        letras = ['B', 'I', 'N', 'G', 'O']

        for letra in letras:
            intervalo = all(intervalos[letra][0] <= x <= intervalos[letra][1] for x in globals()[letra])

            if not intervalo:
                todos_intervalos_ok = False
                for x in globals()[letra]:
                    if not (intervalos[letra][0] <= x <= intervalos[letra][1]):
                        valores_fora_do_intervalo.append(x)

                contador += 1

        if todos_intervalos_ok:
            print("OK")
        else:
            # Agrupa valores fora do intervalo por letra
            valores_fora_por_letra = {letra: [] for letra in letras}
            for x in valores_fora_do_intervalo:
                for letra in letras:
                    if intervalos[letra][0] <= x <= intervalos[letra][1]:
                        valores_fora_por_letra[letra].append(x)
                        break

            # Verifica se há valores em diferentes intervalos
            intervalos_diferentes = sum(1 for valores in valores_fora_por_letra.values() if valores)

            if intervalos_diferentes > 1:
                print("RECICLAVEL")
            else:
                print("DESCARTAVEL")

    except EOFError:
        break