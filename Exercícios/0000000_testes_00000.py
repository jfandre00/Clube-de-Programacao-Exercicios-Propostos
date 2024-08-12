while True:
    try:
        contador = 0
        valores_fora_do_intervalo = [] 
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

        if contador % 2 == 0 and contador != 0:
            #preciso pegar a lista valores_fora_do_intervalo e verificar se os valores dentro dela pertencem a intervalos diferentes, que podem ser trocados. Por exemplo, se tiver um valor pertencente a B e outro a I, podemos trocar de lugar, mas caso tenhamos 2 valores pertencentes a mesma letra não tem como trocar, e a cartela seria descartavel.
            
            print("RECICLAVEL")

        if contador % 2 != 0 and contador != 0:
            print("DESCARTAVEL")

    except EOFError:
        break