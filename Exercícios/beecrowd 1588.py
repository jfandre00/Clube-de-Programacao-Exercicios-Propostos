#beecrowd 1588

def somadorPontos():
    print("oi")


times = []
lista_jogos = []
jogos = []

T = int(input()) #entrada do número de casos
N, M = map(int, input().split()) #entrada de N (nº times) M (nº jogos)

for n in range(N):
    time = input()
    times.append(time) #inserindo os N times na lista

for m in range(M):
    jogo = input()
    jogos = jogo.split()
    
    lista_jogos.append(jogos)

