# Função para verificar se é possível separar os participantes em duas salas
# sem que amigos fiquem juntos
def separacao_possivel(amizades):
    sala1 = set()  # Participantes da sala 1
    sala2 = set()  # Participantes da sala 2

    # Verifica cada participante p
    for p in amizades:
        
        # Caso 1: p tem amigos nas duas salas -> impossível separar
        if len(amizades[p] & sala1) > 0 and len(amizades[p] & sala2) > 0:
            return "NAO"
        
        # Caso 2: p tem amigos na sala 2
        elif len(amizades[p] & sala2) > 0:
            # Se p já está na sala 2 -> impossível
            if p in sala2:
                return "NAO"
            # Caso contrário, p vai para a sala 1
            sala1.add(p)
            # E todos os amigos de p vão para a sala 2
            sala2.update(amizades[p]) # professor usou sala2 |= amizades[p]

        # Caso 3: p não tem amigos na sala 2, mas pode ter na sala 1
        else:
            # Se p tem amigos na sala 1 e já está lá -> impossível
            if len(amizades[p] & sala1) > 0 and p in sala1:
                return "NAO"
            # Caso contrário, p vai para a sala 2
            sala2.add(p)
            # E todos os amigos de p vão para a sala 1
            sala1.update(amizades[p]) # professor usou sala1 |= amizades[p]

    # Se chegou até aqui, é possível separar
    return "SIM"


########################
n = int(input())  # Num de participantes

while n != 0:
    amizades = {}

    for _ in range(n):
        p = input()  # Num do Amigo
        amigos = set(input().split())  # Lista de amigos dentro de um set
        # precisa ser set para podermos usar o update acima (ou o |= que o professor usou)
        amizades[p] = amigos  # Guarda no dicionário

    # Verifica se é possível separar e já imprime o resultado
    print(separacao_possivel(amizades))

    # Lê o próximo caso
    n = int(input())