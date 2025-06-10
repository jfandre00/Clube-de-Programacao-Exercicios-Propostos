#2 provas obrigatórias, p1 e p2 
# quem fez as duas provas, a média final é a média aritmética das duas provas
# quem fez trabalho terá 3 notas, a média final será a média das três notas
# para 4 notas, tem que ter feito o trabalho. a 4ª nota substitui a menor nota das 3. caso a 4ª nota seja menor que a menor das 3, a média final será a média das 3 notas
# se o aluno só fez a p1 a segunda nota é 0

n = int(input()) #quantidade de alunos da turma
alunos = []
medias = []
notas = []
somaNotas = 0

for i in range(n):
    aluno = input().strip()
    alunos.append(aluno)
    notas = list(map(float, input().strip().split()))
    for j in range(len(notas)):
        somaNotas += notas[j]
    if len(notas) == 2:
        media = (notas[0] + notas[1]) / 2
    elif len(notas) == 3:
        media = (notas[0] + notas[1] + notas[2]) / 3
    elif len(notas) == 4:
        menorNota = min(notas[0], notas[1], notas[2])
        if notas[3] < menorNota:
            media = (notas[0] + notas[1] + notas[2]) / 3
        else:
            nova_soma = sum(notas[:3]) - menorNota + notas[3] #substitui a menor nota pela 4ª
            media = nova_soma / 3
    elif len(notas) == 1:
        media = notas[0] / 2
    else:
        media = 0
    medias.append(media)
    notas = []

#imprime a média de cada aluno
for i in range(n):
    print(f'{alunos[i]}: {medias[i]:.1f}')
