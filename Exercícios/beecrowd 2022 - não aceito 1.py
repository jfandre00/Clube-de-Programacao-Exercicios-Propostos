#Exercício beecrowd 2022

Nome, Q = map(str, input().split()) #entrei com nome e tamanho da lista, separei por string
Q = int(Q) #Q é convertido a um inteiro
lista_completa = []

for _ in range(Q):
    item_desejado = []
    O = input()
    P, E = map(float, input().split())
    E = int(E)
    item_desejado.append(E)
    item_desejado.append(P)
    item_desejado.append(O)
    lista_completa.append(item_desejado)

lista_completa.sort(key=lambda x: (-x[0], x[1], x[2]))

print(f'Lista de {Nome}')
for E, P, O in lista_completa:
    print(f'{O} - R${P:.2f}')