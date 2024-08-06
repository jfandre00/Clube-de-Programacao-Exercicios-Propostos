N, S = map(int, input().split())
transacoes = []


for i in range(N):
    transacao = int(input())
    transacoes.append(transacao)

for i in range(len(transacoes)):
    if i == 0:
        menor = S
    S += transacoes[i]
    if S < menor:
        menor = S
    

print(menor)
    
