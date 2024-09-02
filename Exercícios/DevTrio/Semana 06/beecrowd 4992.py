#beecrowd 4992
#input C (número de times), N (tentativas)
# ci (numero do time) pi (numero problema) ti (tempo submissão em segundos) ri (1 se foi aceito, 0 se não)
# output: C inteiros, número do time ordenado pelo ranking

C, N = map(int, input().split())

#como armazenar as entradas, pois podem ter dados de um mesmo time em linhas diferentes
#criar um dicionário com chave sendo o número do time e valor sendo uma lista com os dados de cada tentativa
#ordenar a lista de tentativas de cada time por tempo
#contar quantos problemas cada time resolveu
#ordenar os times pelo número de problemas resolvidos e tempo
#imprimir os times ordenados

times = {}
for i in range(N):
    ci, pi, ti, ri = map(int, input().split())
    if ci not in times:
        times[ci] = []
    times[ci].append([pi, ti, ri])

for i in times:
    times[i].sort(key=lambda x: x[1])

times_ordenados = sorted(times.items(), key=lambda x: (len([y for y in x[1] if y[2] == 1]), sum([y[1] for y in x[1] if y[2] == 1])))
                         
for i in times_ordenados:
    print(i[0], end=' ')          
    print()



