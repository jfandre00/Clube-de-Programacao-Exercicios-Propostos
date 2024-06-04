def process_lista_desejos():
    try:
        while True:
            # Lendo o nome e o tamanho da lista
            entrada = input().strip()
            if not entrada:
                break
            Nome, Q = entrada.split()
            Q = int(Q)

            # Inicializando a lista completa
            lista_completa = []

            # Iterando Q vezes para ler os itens desejados
            for _ in range(Q):
                O = input().strip()  # Nome do objeto desejado
                P, E = map(float, input().strip().split())  # Preço e escala de preferência
                E = int(E)  # Convertendo E para inteiro
                lista_completa.append([E, P, O])

            # Ordenando a lista completa de acordo com os critérios fornecidos
            lista_completa.sort(key=lambda x: (-x[0], x[1], x[2]))

            # Construindo o resultado
            print(f"Lista de {Nome}")
            for E, P, O in lista_completa:
                print(f"{O} - R$ {P:.2f}")
            print("")  # Linha em branco após cada lista
    except EOFError:
        pass

# Executar a função para processar as listas de desejos
process_lista_desejos()