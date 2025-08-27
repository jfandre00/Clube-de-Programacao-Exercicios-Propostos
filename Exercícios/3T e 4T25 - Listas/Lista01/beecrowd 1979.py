#################################################
### confirmar se será aceito pelo juiz online ###
#################################################
#                     GRAFOS                    #

def eh_bipartido(n, dicionario_amigos):

    salas = {i: 0 for i in range(1, n + 1)} # Dicionario criado vazio com n amigos
    
    # Precisamos testar para cada aluno, pois o grupo de amigos pode ser desconectado
    # Ex: Alunos 1-2-3 são amigos entre si, e 4-5-6 são amigos entre si, mas ninguém do
    # primeiro grupo conhece alguém do segundo
    for aluno_inicial in range(1, n + 1):
        # Se o aluno ainda não foi colorido, começamos uma busca a partir dele
        if salas[aluno_inicial] == 0:
            # Fila para a busca em largura (BFS). Começamos com o aluno atual.
            fila = [aluno_inicial]
            salas[aluno_inicial] = 1 # Coloca o primeiro na Sala 1

            while fila:
                # Pega o primeiro aluno da fila
                aluno_atual = fila.pop(0)
                
                # Para cada amigo do aluno atual
                if aluno_atual in dicionario_amigos:
                    for amigo in dicionario_amigos[aluno_atual]:
                        # Se o amigo ainda não tem cor
                        if salas[amigo] == 0:
                            # Coloca o amigo na sala oposta (pois os amigos não podem estar na mesma sala)
                            salas[amigo] = -1 * salas[aluno_atual]
                            # Adiciona o amigo na fila para visitar seus amigos depois
                            fila.append(amigo)
                        # Se o amigo JÁ TEM a MESMA cor do aluno atual, não temos como atender a solicitação de separação, nem precisa continuar
                        elif salas[amigo] == salas[aluno_atual]:
                            # IMPOSSÍVEL! Retorna Falso.
                            return False
    
    # Se chegamos até aqui, significa que conseguimos alocar todo mundo sem conflitos.
    return True




while True:
    n = int(input())

    if n == 0:
        break

    # Vamos usar um dicionário para representar as amizades (grafo)
    # A chave será o ID do aluno, e o valor será uma lista de seus amigos
    amigos = {i: [] for i in range(1, n + 1)}

    # Lê as N listas de amizade
    for _ in range(n):
        id_aluno = int(input().strip())

        # Lê a lista de amigos (sempre existe pelo menos 1 amigo)
        lista_amigos = list(map(int, input().split()))
        amigos[id_aluno] = lista_amigos # Adicionamos ao dicionario acima


    # Chama a função que verifica se é possível separar os alunos
    if eh_bipartido(n, amigos):
        print("SIM")
    else:
        print("NAO")
