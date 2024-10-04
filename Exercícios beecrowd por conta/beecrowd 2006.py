t = int(input())
respostas = list(map(int, input().split()))

acertos = 0

for resposta in respostas:
    if resposta == t:
        acertos += 1

print(acertos)