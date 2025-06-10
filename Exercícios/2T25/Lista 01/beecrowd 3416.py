# N estudantes matriculados
# L litros de café por vez
# não é possível preparar menos que L litros por vez
# cada estudante bebe D mililitros de café por aula
# qual é a quantidade mínima de café que deve ser preparada para atender a todos os estudantes

n, l, d = map(int, input().split())

quantidadeMinimaDeCafe = n * d / 1000

if quantidadeMinimaDeCafe % l == 0:
    quantidadeMinimaDeCafe = int(quantidadeMinimaDeCafe / l)
else:
    quantidadeMinimaDeCafe = int(quantidadeMinimaDeCafe / l) + 1

print(quantidadeMinimaDeCafe*l)


