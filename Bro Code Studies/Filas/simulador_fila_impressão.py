from filas import Fila

def simulador(eventos):
    eventos = eventos.split(",")
    fila_impressao = Fila()
    tarefa_atual = None
    tempo_tarefa_atual = 0
    cont_tarefas = 0

    for tempo, e in enumerate(eventos):
        print(f"\nTempo: {tempo}:")
        #Nova tarefa recebida
        if e.startswith("t"):
            cont_tarefas += 1
            fila_impressao.enfileira({"id_tar": cont_tarefas, "duracao": int(e[1:])})

        #Imprimir status da fila
        elif e == "s":
            print(f"Fila: {fila_impressao}")
        #Se há uma tarefa em execução:
        if tarefa_atual:
            tempo_tarefa_atual += 1
            #Se o tempo de processamento = duracao da tarefa:
            if tempo_tarefa_atual == tarefa_atual["duracao"]:
                print(f"Tarefa {tarefa_atual} concluída")
                tarefa_atual = None
            else:
                print(f"Processando tarefa {tarefa_atual}")
        #Se a impressora está livre e há tarefas na fila:
        elif not fila_impressao.vazia():
            tarefa_atual = fila_impressao.desenfileira()
            tempo_tarefa_atual = 0

simulador("t3,t1,t2,s,,t3,,,s,,,,s")
