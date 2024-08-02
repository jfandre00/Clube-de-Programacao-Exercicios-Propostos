#beecrowd 2176

'''S = mensagem que será enviada de um dispositivo para outro
um bit extra B é adicionado ao final da representação binária de S
if S == número par de bits de valor 1 -> bit extra B será 0
if S == número ímpar de bits de valor 1 -> bit extra B será 1
Após a inserção do bit B, a mensagem S terá um número par de bits de valor 1

mensagem recebida -> contagem de bits de valor 1
    Se for par -> mensagem chegou com sucesso
    Se for ímpar -> sofreu alteração e não está correta

A tarefa é escrever um algorítmo que faça a inserção do bit B na mensagem S, de forma que após a inserção a mensagem S tenha um número par de bits de valor 1'''

S = str(input())
contador_de_1 = 0

for i in range (0, len(S)):
    if S[i] == '1':
        contador_de_1 += 1

if contador_de_1 % 2 == 0:
    add="0"
else:
    add="1"

print(S+add)