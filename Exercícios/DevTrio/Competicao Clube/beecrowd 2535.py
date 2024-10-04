#N filhotes para adoção
#animal deve ser cachorro
#animal deve ter nome composto
#pelo menos uma das palavras do nome composto deve começar com o mesmo caractere do nome da raça

while True:
    try:
        # Lê o número de filhotes (N)
        N = int(input().strip())

        count = 0  # Contador de filhotes que cumprem as exigências

        for _ in range(N):
            especie = input().strip()  # Leitura da espécie do animal
            raca = input().strip()  # Leitura da raça
            nome = input().strip()  # Leitura do nome
            input().strip()  # Ignorar a linha em branco

            if especie == 'cachorro':  # Verifica se é da espécie cachorro
                # Verifica se o nome é composto (mais de uma palavra)
                if len(nome.split()) > 1:
                    # Verifica se alguma palavra do nome começa com o mesmo caractere que a raça
                    for palavra in nome.split():
                        if palavra[0].lower() == raca[0].lower():
                            count += 1
                            break  # Pode parar de verificar este filhote

        print(count)
    
    except EOFError:
        break
