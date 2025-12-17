while True:
    linha = input().strip()
    if linha == ".":
        break

    palavras = linha.split()

    # Conta quantas vezes cada palavra aparece
    contagem = {}
    for p in palavras:
        if p in contagem:
            contagem[p] += 1
        else:
            contagem[p] = 1

    # Para cada letra, escolhe a palavra que gera mais economia
    abreviacoes = {}
    for p, qtd in contagem.items():
        letra = p[0]
        economia = (len(p) - 2) * qtd
        if economia > 0:
            if letra not in abreviacoes or economia > abreviacoes[letra][1]:
                abreviacoes[letra] = (p, economia)

    # Cria o mapeamento final: palavra -> abreviação
    mapa = {}
    for letra, (p, _) in abreviacoes.items():
        mapa[p] = f"{letra}."

    # Substitui as palavras no texto
    resultado = []
    for p in palavras:
        if p in mapa:
            resultado.append(mapa[p])
        else:
            resultado.append(p)
    print(" ".join(resultado))

    # Imprime as abreviações em ordem alfabética
    print(len(abreviacoes))
    for letra in sorted(abreviacoes):
        print(f"{letra}. = {abreviacoes[letra][0]}")