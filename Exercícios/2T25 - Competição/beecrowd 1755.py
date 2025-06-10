t = int(input())

for _ in range(t):
    d, n = map(int, input().split())
    precos = list(map(float, input().split()))

    d_centavos = int(round(d * 100))
    lista_trocos = []

    for preco in precos:
        preco_centavos = int(round(preco * 100))
        if preco_centavos == 0:
            continue  # ignorar preço inválido
        quantidade = d_centavos // preco_centavos
        if quantidade == 0:
            continue  # não pode comprar nenhuma unidade
        troco = d_centavos - (quantidade * preco_centavos)
        lista_trocos.append(troco)

    if lista_trocos:
        maior_troco = max(lista_trocos)
        print(f"{maior_troco / 100:.2f}")
    else:
        print("0.00")  