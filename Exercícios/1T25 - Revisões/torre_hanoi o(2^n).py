def cria_torres():
    return[['#' * (2 * i -1) for i in range(n_discos +1, 1, -1)], [], []]

def imprime_torres(torres):
    print()
    for i in range(n_discos -1, -1, -1):
        for j in range(3):
            print(f"{torres[j][i] if i < len(torres[j]) else '':^25}", end='')
        print()
    print(f"{1:^25}{2:^25}{3:^25}")

def torre_hanoi(torres, n, origem=0, destino=2, auxiliar=1):
    movimentos = 0
    if n > 0:
        # Move N - 1 discos da torre de origem para a torre auxiliar
        movimentos += torre_hanoi(torres, n - 1, origem, auxiliar, destino)
        # Move 1 disco da torre de origem para a torre de destino
        torres[destino].append(torres[origem].pop())
        movimentos += 1
        #Imprime estado das torres
        imprime_torres(torres)
        # Move N - 1 discos da torre auxiliar para a torre de destino
        movimentos += torre_hanoi(torres, n - 1, auxiliar, destino, origem)

    return movimentos

n_discos = int(input("Digite o número de discos (máx 8): "))
if not 1 <= n_discos <= 8:
    print("Número de discos inválido")
else:
    torres = cria_torres()
    imprime_torres(torres)
    movimentos = torre_hanoi(torres, n_discos)
    print(f"Torre de Hanoi resolvida em {movimentos} movimentos")

