def determinar_vencedor(nome1, escolha1, nome2, escolha2, n, m):
    soma = n + m
    if soma % 2 == 0:
        if escolha1 == "PAR":
            return nome1
        else:
            return nome2
    else:
        if escolha1 == "IMPAR":
            return nome1
        else:
            return nome2

QT = int(input())

for _ in range(QT):
    jogador1, escolha1, jogador2, escolha2 = input().split()
    
    n, m = map(int, input().split())
    
    vencedor = determinar_vencedor(jogador1, escolha1, jogador2, escolha2, n, m)
    print(vencedor)