while True:
    # Lê N (quantidade de pessoas)
    N = int(input().strip())

    # Se N = 0, encerra
    if N == 0:
        break

    # Lê a linha com os tempos
    tempos = list(map(int, input().split()))

    # A escada começa desligada.
    # Vamos controlar até quando ela ficará ligada.
    fim_ativo = 0  # tempo onde a escada desliga
    total = 0      # tempo total ligada

    for t in tempos:
        # Cada pessoa liga por 10 segundos: intervalo [t, t+9]
        inicio = t
        fim = t + 10  # usamos t+10 porque o segundo t+10 já está desligada

        if inicio >= fim_ativo:
            # Não há sobreposição com o intervalo anterior
            # Somamos os 10 segundos completos
            total += 10
            fim_ativo = fim
        else:
            # Existe sobreposição, então só estende se necessário
            if fim > fim_ativo:
                total += (fim - fim_ativo)
                fim_ativo = fim
            # Caso contrário, toda a duração já está coberta e não somamos nada

    print(total)