

teste = 1
aeroportos, voos = map(int, input().split())

while aeroportos != 0 and voos != 0:
    
    lista_de_aeroportos = [0] * (aeroportos) 


    for _ in range(voos):
        a, b = map(int, input().split())
        lista_de_aeroportos[a - 1] += 1
        lista_de_aeroportos[b - 1] += 1

    print(f"Teste {teste}")

    # Se tiver mais de 1 aeropoto com o maior número de voos, mostar os dois separados por espaço
    maior = max(lista_de_aeroportos)
    for i, v in enumerate(lista_de_aeroportos):
        if v == maior:
            print(i + 1, end=" ")
    print()
    print()
    teste += 1
    aeroportos, voos = map(int, input().split())