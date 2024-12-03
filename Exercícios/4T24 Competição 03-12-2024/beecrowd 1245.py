def calcular_pares_botas():
    while True:
        try:
            n = int(input())  
            botas_direitas = {}
            botas_esquerdas = {}

            for _ in range(n):
                tamanho, lado = input().split()
                tamanho = int(tamanho)
                
                if lado == 'D':
                    if tamanho not in botas_direitas:
                        botas_direitas[tamanho] = 0
                    botas_direitas[tamanho] += 1
                
                elif lado == 'E':
                    if tamanho not in botas_esquerdas:
                        botas_esquerdas[tamanho] = 0
                    botas_esquerdas[tamanho] += 1

            pares = 0
            for tamanho in botas_direitas:
                if tamanho in botas_esquerdas:
                    pares += min(botas_direitas[tamanho], botas_esquerdas[tamanho])

            print(pares)

        except EOFError:
            break

calcular_pares_botas()