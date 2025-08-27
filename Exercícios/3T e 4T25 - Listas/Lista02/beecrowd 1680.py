# Lista de deslocamentos para cada direção
movimentos = [
    (10, 0),   # Direita: soma 10 no X
    (0, 10),   # Cima: soma 10 no Y
    (-10, 0),  # Esquerda: subtrai 10 no X
    (0, -10)   # Baixo: subtrai 10 no Y
]

while True:
    try:
        sequencia = input()
    except EOFError:
        break

    # Coordenadas iniciais independente da entrada
    x = 300
    y = 420

    # Direção inicial é direita -> índice 0 na lista movimentos
    direcao = 0

    # Comando inicial: posiciona a caneta no ponto inicial
    print(f"{x} {y} moveto")

    # Primeiro movimento que é SEM depender da string, obrigatório
    # Sempre vai 10 unidades para a direita!
    x += movimentos[direcao][0]
    y += movimentos[direcao][1]
    print(f"{x} {y} lineto")



    # Utilização do %4??
    # Ele garante que a direção sempre fica no intervalo 0 a 3, mesmo quando:
    # Somamos e passamos de 3 (vira para esquerda de 3 -> 0)
    # Subtraímos e ficamos negativos (vira para direita de 0 -> 3)
    # É como um ciclo de direções

    for caractere in sequencia: # Vamos percorrer as letras do input
        if caractere == 'A':
            # Gira 90 graus para a direita (sentido horário)
            # Equivalente a diminuir 1 na direção
            direcao = (direcao + 3) % 4
        elif caractere == 'V':
            # Gira 90 graus para a esquerda (sentido anti-horário)
            # Equivalente a aumentar 1 na direção
            direcao = (direcao + 1) % 4

        # Move 10 unidades na nova direção
        x += movimentos[direcao][0]
        y += movimentos[direcao][1]
        print(f"{x} {y} lineto")

    # Finaliza com o padrão
    print("stroke")
    print("showpage")

