'''Entrada -> A primeira linha de entrada contém um número inteiro QT (1 ≤ QT ≤ 100), indicando a quantidade de casos de teste que vem a seguir. Cada caso de teste contém duas linhas. Na primeira linha será informado o nome do jogador 1 seguido de sua escolha, “PAR” ou “IMPAR” e logo após, o nome do jogador 2 seguido de sua escolha, “PAR” ou “IMPAR”. Na segunda linha de entrada, contém 2 números inteiros N (1 ≤ N ≤ 10⁹) e M (1 ≤ M ≤ 10⁹), representando respectivamente os números escolhidos pelo jogador 1 e pelo jogador 2. É garantido que a escolha (PAR ou IMPAR) do jogador 1 será diferente da escolha (PAR ou IMPAR) do jogador 2 e que o nome dos jogares são formados somente por letras e não ultrapassarão 100 caracteres.

Saída -> Para cada caso de teste, imprima uma única linha contendo o nome do jogador vencedor.
'''

def validarNumeroJogadas(jogadas):
    while True:
        if jogadas not in range(1,101):
            jogadas = int(input("Erro! Número fora do alcance! Entre novamente: "))
        else:
            return jogadas
            break

def validarEscolhaNumero(numero):
    while True:
        if numero not in range(1,1000000001):
            numero = int(input(f'Erro! o número escolhido por {nome1} está fora do alcance! Entre novamente: '))
        else:
            return numero
            break

def validarParOuImpar(escolha1, escolha2):
    if validarEscolhaIgual(escolha1, escolha2):
        while True:
            if escolha1.upper() in ['PAR', 'IMPAR']:
                break
            else:
                escolha1 = input(f'Erro! {nome1}, escolha PAR ou IMPAR: ')
        while True:
            if escolha2.upper() in ['PAR', 'IMPAR']:
                break
            else:
                escolha2 = input(f'Erro! {nome2}, escolha PAR ou IMPAR: ')

def validarEscolhaIgual(escolha1, escolha2):
    while True:
        if escolha1.upper() == escolha2.upper():
            escolha1, escolha2 = list(map(str, input(f"ERRO! Não podem ser iguais! Entre com a escolha dos 2 jogadores (PAR/IMPAR) separado por espaço: ").split()))
        else:
            return True
            break

def quemVenceu(N,M):
    if (N + M) % 2 == 0:
        if escolha1.upper() == 'PAR':
            print(f'{nome1} venceu pois escolheu PAR')    
        else:
            print(f'{nome2} venceu pois escolheu PAR') 
    else:
        if escolha1.upper() == 'IMPAR':
            print(f'{nome1} venceu pois escolheu IMPAR')    
        else:
            print(f'{nome2} venceu pois escolheu IMPAR') 
    


qt = int(input("Entre com o número de jogadas de PAR ou IMPAR (entre 1 e 100): "))
validarNumeroJogadas(qt)


for _ in range(qt):
    nome1, escolha1, nome2, escolha2 = list(map(str, input(f"Entre com o nome e a escolha dos 2 jogadores (PAR/IMPAR)separado por espaço: ").split()))  
    validarParOuImpar(escolha1, escolha2)

    N, M = list(map(int, input(f'Entre com os números escolhidos por {nome1} e {nome2} separado por espaço').split()))
    validarEscolhaNumero(N)
    validarEscolhaNumero(M)
    quemVenceu(N,M)

    

