while True:
    try:
        contador = 0

        numeros = list(map(int, input().split()))

        numeros.insert(12,0) #pois temos um valor que não é preenchido em linha 3 - "N"

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

        N.remove(0) #removendo o 0 já que os números estão corretamente separados agora

        intervalos = {
            'B': (1, 15),
            'I': (16, 30),
            'N': (31, 45),
            'G': (46, 60),
            'O': (61, 75) } #intervalos para cada coluna

        # Verifica se todos os elementos estão no intervalo do dicionário acima
        intervalo_B = all(intervalos['B'][0] <= x <= intervalos['B'][1] for x in B)
        if intervalo_B == False:
            contador += 1
        intervalo_I = all(intervalos['I'][0] <= x <= intervalos['I'][1] for x in I)
        if intervalo_I == False:
            contador += 1
        intervalo_N = all(intervalos['N'][0] <= x <= intervalos['N'][1] for x in N)
        if intervalo_N == False:
            contador += 1
        intervalo_G = all(intervalos['G'][0] <= x <= intervalos['G'][1] for x in G)
        if intervalo_G == False:
            contador += 1
        intervalo_O = all(intervalos['O'][0] <= x <= intervalos['O'][1] for x in O)
        if intervalo_O == False:
            contador += 1

        if intervalo_B and intervalo_I and intervalo_N and intervalo_G and intervalo_O:
            print("OK")

        if contador % 2 == 0 and contador != 0:
            print("RECICLAVEL")

        if contador % 2 != 0 and contador != 0:
            print("DESCARTAVEL")

    except EOFError:
        break