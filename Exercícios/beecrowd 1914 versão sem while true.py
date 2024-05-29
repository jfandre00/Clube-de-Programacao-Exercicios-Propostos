def validarNumeroJogadas(jogadas):
    while jogadas not in range(1, 101):
        jogadas = int(input("Erro! Número fora do alcance! Entre novamente: "))
    return jogadas

def validarEscolhaNumero(numero, jogador):
    while numero not in range(1, 1000000001):
        numero = int(input(f'Erro! o número escolhido por {jogador} está fora do alcance! Entre novamente: '))
    return numero

def validarParOuImpar(escolha, jogador):
    while escolha.upper() not in ['PAR', 'IMPAR']:
        escolha = input(f'Erro! {jogador}, escolha PAR ou IMPAR: ')
    return escolha.upper()

def validarEscolhaIgual(escolha1, escolha2):
    while escolha1 == escolha2:
        escolha1, escolha2 = input(f"ERRO! Não podem ser iguais! Entre com a escolha dos 2 jogadores (PAR/IMPAR) separado por espaço: ").split()
        escolha1 = validarParOuImpar(escolha1, "jogador 1")
        escolha2 = validarParOuImpar(escolha2, "jogador 2")
    return escolha1, escolha2

def quemVenceu(N, M, nome1, escolha1, nome2, escolha2):
    soma = N + M
    if soma % 2 == 0:
        if escolha1 == 'PAR':
            print(f'{nome1} venceu pois escolheu PAR')    
        else:
            print(f'{nome2} venceu pois escolheu PAR') 
    else:
        if escolha1 == 'IMPAR':
            print(f'{nome1} venceu pois escolheu IMPAR')    
        else:
            print(f'{nome2} venceu pois escolheu IMPAR') 

# Programa principal
qt = int(input("Entre com o número de jogadas de PAR ou IMPAR (entre 1 e 100): "))
qt = validarNumeroJogadas(qt)

for _ in range(qt):
    nome1, escolha1, nome2, escolha2 = input("Entre com o nome e a escolha dos 2 jogadores (PAR/IMPAR) separado por espaço: ").split()
    escolha1 = validarParOuImpar(escolha1, nome1)
    escolha2 = validarParOuImpar(escolha2, nome2)
    escolha1, escolha2 = validarEscolhaIgual(escolha1, escolha2)
    
    N, M = map(int, input(f'Entre com os números escolhidos por {nome1} e {nome2} separados por espaço: ').split())
    N = validarEscolhaNumero(N, nome1)
    M = validarEscolhaNumero(M, nome2)
    
    quemVenceu(N, M, nome1, escolha1, nome2, escolha2)