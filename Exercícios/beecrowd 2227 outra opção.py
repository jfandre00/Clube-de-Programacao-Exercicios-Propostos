teste = 1  # Número do teste, começando em 1
while True:
    # Lê a quantidade de aeroportos (a) e voos (v)
    a, v = map(int, input().split())

    # Verifica se é o fim da entrada
    if a == 0 and v == 0:
        break

    # Cria uma lista para contar os voos de cada aeroporto
    voos_por_aeroporto = [0] * a

    # Lê cada voo e atualiza os contadores de voos dos aeroportos
    for _ in range(v):
        x, y = map(int, input().split())
        voos_por_aeroporto[x - 1] += 1
        voos_por_aeroporto[y - 1] += 1

    # Encontra o número máximo de voos em qualquer aeroporto
    max_voos = max(voos_por_aeroporto)

    # Encontra todos os aeroportos que têm esse número máximo de voos
    aeroportos_mais_movimentados = [str(i + 1) for i in range(a) if voos_por_aeroporto[i] == max_voos]

    # Imprime o resultado formatado conforme especificado
    print(f'Teste {teste}')
    print(' '.join(aeroportos_mais_movimentados))
    print()  # Linha em branco entre os testes

    # Incrementa o número do teste
    teste += 1