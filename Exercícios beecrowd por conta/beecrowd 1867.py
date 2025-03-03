while True:
    N, M = map(str, input().split())
    if N == '0' and M == '0':
        break
    somaN, somaM = 0, 0

    tamanhoN = len(N)
    tamanhoM = len(M)

    while len(N) != 1:
        somaN = 0
        for i in range(tamanhoN):
            somaN += int(N[i])
        N = str(somaN)
        tamanhoN = len(N)

    while len(M) != 1:
        somaM = 0
        for i in range(tamanhoM):
            somaM += int(M[i])
        M = str(somaM)
        tamanhoM = len(M)

    if int(N) > int(M):
        print(1)
    elif int(N) < int(M):
        print(2)
    else:
        print(0)




