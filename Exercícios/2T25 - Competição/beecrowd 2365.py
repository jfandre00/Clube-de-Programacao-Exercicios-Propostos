
listao = []
lista_gabarito = []

p, n = map(int, input().split())
for i in range(p):
    nome = input()
    for j in range(n):
        timeA, golA, timeB, golB = map(str, input().split())
        golA = int(golA)
        golB = int(golB)
    listao.append((golA, golB, nome))
for j in range(n):
    gabaritoA, golA, gabaritoB, golB = map(str, input().split())
    golA = int(golA)
    golB = int(golB)
    lista_gabarito.append((golA, golB))

# regras : 10 pontos se acertou exatamente golA e golB
# 7 pontos se acertou quem ganhou e os gols marcados por um time
# 5 pontos se acertou apenas o resultado (quem ganhou e quem perdeu)
# 2 pontos se acertou os gols de um time, mas não o resultado
# 0 pontos se não acertou nada

pontuacao = 0

for i in range(p):
    golA, golB, nome = listao[i]
    gabaritoA, gabaritoB = lista_gabarito[i]
    
    if golA == gabaritoA and golB == gabaritoB:
        pontuacao += 10
    elif (golA > golB and gabaritoA > gabaritoB) or (golA < golB and gabaritoA < gabaritoB):
        pontuacao += 7
        if golA == gabaritoA or golB == gabaritoB:
            pontuacao += 2
    elif (golA > golB and gabaritoA < gabaritoB) or (golA < golB and gabaritoA > gabaritoB):
        pontuacao += 5
    elif golA == gabaritoA or golB == gabaritoB:
        pontuacao += 2
    # imprimir o nome do time e a pontuação e fazer isso para todos os times
print(f"{nome} {pontuacao}")

