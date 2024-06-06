#beecrowd #2022
def processar_listas():
    while True:
        try:
            linha = input().strip()
            if not linha:
                break

            # Lê o nome do dono da lista e a quantidade de presentes
            nome, Q = linha.split()
            Q = int(Q)
            presentes = []

            # Lê cada presente e suas informações
            for _ in range(Q):
                O = input().strip()
                P, E = input().strip().split()
                P = float(P)
                E = int(E)
                presentes.append((O, P, E))

            # Ordena os presentes
            presentes.sort(key=lambda x: (-x[2], x[1], x[0]))

            # Imprime a lista formatada
            print(f'Lista de {nome}')
            for presente in presentes:
                print(f'{presente[0]} - R${presente[1]:.2f}')
            print()
        except EOFError:
            break

# Para executar a função, chame processar_listas()
if __name__ == "__main__":
    processar_listas()

'''Esse código é uma função chamada processar_listas que lê a entrada de dados sobre presentes de Natal de várias pessoas. Ele faz o seguinte:

Leitura dos Dados: Para cada pessoa, o código lê o nome do dono da lista e a quantidade de presentes que essa pessoa deseja.

Processamento dos Presentes: Para cada presente da pessoa, o código lê o nome do presente, o preço e a preferência (um número de 1 a 10, onde 10 é o mais desejado).

Ordenação: Os presentes são ordenados primeiro pela preferência (do maior para o menor), depois pelo preço (do menor para o maior) e, se houver empate, pelo nome em ordem alfabética.

Saída Formatada: Para cada pessoa, o código imprime a lista de presentes ordenada, mostrando o nome do presente, o preço e a preferência, formatando o preço com duas casas decimais. Cada lista é precedida pelo nome do dono da lista.

Finalização: O código termina quando não houver mais linhas de entrada.

Em resumo, o código lê e processa listas de presentes de Natal, organizando os presentes de cada pessoa de acordo com sua preferência, preço e ordem alfabética. No código fornecido, as variáveis utilizadas são:

linha: Armazena a linha atual lida da entrada. 
nome: Armazena o nome do dono da lista de presentes. 
Q: Armazena a quantidade de presentes na lista. 
presentes: Lista que armazena as informações de cada presente (nome, preço, preferência). 
O: Nome do presente. 
P: Preço do presente. 
E: Preferência do presente. 
Além disso, a função não utiliza explicitamente o nome da exceção no except, apenas EOFError, que indica o final de arquivo durante a leitura da entrada padrão.'''