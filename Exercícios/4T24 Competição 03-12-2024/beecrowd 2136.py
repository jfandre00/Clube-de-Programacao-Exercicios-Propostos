# Entrada de dados
inscricoes = []
while True:
    entrada = input()
    if entrada == "FIM":
        break
    nome, escolha = entrada.rsplit(maxsplit=1)
    inscricoes.append((nome, escolha))

# Separar os que escolheram "YES" e "NO"
amigos_yes = []
amigos_no = []

for nome, escolha in inscricoes:
    if escolha == "YES":
        amigos_yes.append(nome)
    else:
        amigos_no.append(nome)

# Remover duplicatas dos "YES" e manter a ordem de inscrição com um dicionário
amigos_yes = list(dict.fromkeys(amigos_yes))

# Ordenar os dois grupos alfabeticamente
amigos_yes.sort()
amigos_no.sort()

# Encontrar o vencedor entre os "YES"
# Critério: Maior número de letras no nome, em caso de empate, primeiro inscrito.
vencedor = max(
    amigos_yes,
    key=lambda nome: (len(nome), -inscricoes.index((nome, "YES")))
)

# Imprimir a lista organizada
for amigo in amigos_yes:
    print(amigo)
for amigo in amigos_no:
    print(amigo)

# Linha em branco
print()

# Imprimir o vencedor
print("Amigo do Habay:")
print(vencedor)