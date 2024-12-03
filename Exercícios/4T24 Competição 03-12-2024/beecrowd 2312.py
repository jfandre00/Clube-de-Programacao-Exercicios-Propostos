def ordenar_quadro_medalhas(paises):
    return sorted(
        paises,
        key=lambda x: (-x[1], -x[2], -x[3], x[0])
    )

n = int(input())
paises = []

for _ in range(n):
    entrada = input().split()
    nome = entrada[0]
    ouro, prata, bronze = map(int, entrada[1:])
    paises.append((nome, ouro, prata, bronze))

paises_ordenados = ordenar_quadro_medalhas(paises)

for pais in paises_ordenados:
    print(f"{pais[0]} {pais[1]} {pais[2]} {pais[3]}")
