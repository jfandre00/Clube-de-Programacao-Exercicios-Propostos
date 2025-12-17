while True:
    N = int(input().strip())

    if N == 0:
        break

    resultados = list(map(int, input().split()))

    mary = 0
    john = 0

    for resultado in resultados:
        if resultado == 0:
            mary += 1
        else:
            john += 1

    print(f"Mary won {mary} times and John won {john} times")
