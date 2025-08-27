while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    primeira_hora = h1 * 60 + m1
    segunda_hora = h2 * 60 + m2

    diferenca = segunda_hora - primeira_hora
    if diferenca < 0:
        # nessa verificação já entra o caso do 0, não preciso fazer outra
        diferenca += 24 * 60 #vamos somar 1440 (1 dia inteiro) pois o resultado deu negativo

    print(diferenca)