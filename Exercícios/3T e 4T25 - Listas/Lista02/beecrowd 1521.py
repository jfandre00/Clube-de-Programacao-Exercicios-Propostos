while True:
    N = int(input())
    if N == 0:
        break

    lista_de_entregados = list(map(int, input().split()))
    primeiro_a_ser_entrevistado = int(input())

    atual = primeiro_a_ser_entrevistado #vamos comecar pelo primeiro a ser entrevistado, ao inves de inserir ele na lista de entrevistados

    while True: #porque com certeza terá um culpado, então certamente irá sair do loop
        if lista_de_entregados[atual - 1] == atual:
            print(atual)
            break
        else:
            atual = lista_de_entregados[atual - 1]