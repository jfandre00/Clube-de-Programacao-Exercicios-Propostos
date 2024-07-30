t = int(input())

for _ in range(t):
    n,m = (int(x) for x in input().split())
    estatisticas = {}
    for i in range(n):
        time = input()
        # [pontos, vitórias, gols, pos_entrada, nome]
        estatisticas[time] = [0, 0, 0, -i, time]
    for _ in range(m):
        #Ler dados do jogo
        placar = input().split()

        time1, time2 = placar[1], placar[3]
        gols1, gols2 = int(placar[0]), int(placar[2])
        estatisticas[time1][2] += gols1
        estatisticas[time2][2] += gols2
        if gols1 > gols2:
            estatisticas[time1][0] += 3
            estatisticas[time1][1] += 1
            #aumenta 3 pontos e 1 vitória
        elif gols2 > gols1:
            estatisticas[time2][0] += 3
            estatisticas[time2][1] += 1
        else:
            estatisticas[time1][0] += 1
            estatisticas[time2][0] += 1
            #empate 1 ponto para cada

        tabela = [estatisticas[t] for t in estatisticas]
        tabela.sort(reverse=True)
        
        for e in tabela:
            print(e[-1])