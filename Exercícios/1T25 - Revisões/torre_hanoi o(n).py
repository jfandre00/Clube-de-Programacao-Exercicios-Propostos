def torre_hanoi(n):
    if n == 1:
        return 1
    return 2 * torre_hanoi(n - 1) + 1

n = int(input("Digite o número de discos (máx 64): "))
t = 0
while n > 0:
    t += 1
    print("Teste", t)
    print(torre_hanoi(n))
    print()
    n = int(input("Digite o número de discos (máx 64): "))