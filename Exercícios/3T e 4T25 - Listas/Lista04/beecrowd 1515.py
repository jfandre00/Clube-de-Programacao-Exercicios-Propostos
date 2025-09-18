caso_teste = int(input())

while caso_teste != 0:
    primeira_civilizacao = ''
    enviou_em = 0
    for i in range(caso_teste):
        lista_entrada = list(map(str, input().split()))
        a = lista_entrada[0]
        b = int(lista_entrada[1])
        c = int(lista_entrada[2])
        anos = b - c
        if i == 0:
            primeira_civilizacao = a
            enviou_em = anos
            continue
        if anos < enviou_em:
            enviou_em = anos
            primeira_civilizacao = a
    print(primeira_civilizacao)
    caso_teste = int(input())
        