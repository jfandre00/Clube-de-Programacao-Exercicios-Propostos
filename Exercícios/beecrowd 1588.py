#beecrowd 1588

# Função para processar cada caso de forma isolada
def processar_caso(N, M, times, resultados):
    # 1. Inicializa os dados dos times
    dados = {time: {'pontos': 0, 'vitorias': 0, 'gols': 0, 'posicao': i} for i, time in enumerate(times)}

    # 2. Processa os resultados dos jogos
    for resultado in resultados:
        golsA, timeA, golsB, timeB = resultado #separando os dados dos jogos que foi fornecido na entrada em 4 variáveis para testarmos
        golsA = int(golsA)
        golsB = int(golsB)

        if golsA > golsB:
            dados[timeA]['pontos'] += 3  #acessando o dicionário dados, dentro do time: na outra chave (pontos ou vitória)
            dados[timeA]['vitorias'] += 1
        elif golsA < golsB:
            dados[timeB]['pontos'] += 3
            dados[timeB]['vitorias'] += 1
        else:
            dados[timeA]['pontos'] += 1
            dados[timeB]['pontos'] += 1

        dados[timeA]['gols'] += golsA
        dados[timeB]['gols'] += golsB

    # 3. Ordena os times conforme enunciado
    #sorted irá ordenar os itens do dicionário dados conforme a ordem do enunciado. primeiro times com mais pontos, depois mais vitorias, depois mais gols e por fim o índice na lista de entrada. Os item estão negativos pois o retorno do sorted é do menor para o maior, e queremos o contrário, a não ser no caso do index da lista.
    #lambda é quem cria a função com as escolhas.
    times_ordenados = sorted(dados.items(), key=lambda item: (-item[1]['pontos'], -item[1]['vitorias'], -item[1]['gols'], item[1]['posicao']))
    return [time for time, _ in times_ordenados]

# Lê a entrada e processa cada caso
T = int(input())  # Número de casos de teste
resultados_finais = []

for _ in range(T): #vai rodar toda a função para cada caso T
    N, M = map(int, input().split())
    times = [input().strip() for _ in range(N)]
    resultados = [input().split() for _ in range(M)]

    os_times = processar_caso(N, M, times, resultados)
    resultados_finais.extend(os_times)
    #A função processar_caso vai retornar uma lista de resultados para cada caso T, já ordenado
    #a função extend vai adicionando a lista retornada de casa caso T (os_times) ao final da outra lista (resultados_finais), que irá mostrar tudo de uma vez na tela no fim do processo todo, conforme enunciado.

# Imprime os resultados
for time in resultados_finais:
    print(time)

'''
Enunciado:
A federação de futebol te contratou para elaborar a classificação dos times do campeonato. Você vai receber uma lista com alguns jogos ocorridos e deve ordenar os times. Uma vitória garante 3 pontos ao time, um empate 1 ponto e uma derrota 0 pontos.

Leia atentamente a seguir o regulamento sobre como a classificação deve ser feita: Primeiramente o time com mais pontos deve ficar em primeiro. Caso haja empate, o time com mais vitórias fica na frente. Caso ainda tenha empate, o time com mais gols fica na frente. Por último se nenhum dos critérios acima possa desempatar os times, o que aparecer primeiro na entrada fica na frente.

Dado os times e os jogos que já aconteceram, ordene e imprima o nome dos times na ordem de classificação.

Entrada
Na primeira linha teremos um inteiro T (T ≤ 100), indicando o número de casos de teste.

Na primeira linha de cada caso teremos dois números, N (2 ≤ N ≤ 20* ou 2 ≤ N ≤ 100**) e M (1 ≤ M ≤ 100* ou 1 ≤ M ≤ 1000**), indicando quantos times estão no campeonato e quantos jogos já aconteceram. Nas próximas N linhas teremos os nomes dos times, que são únicos, contendo apenas letras minúsculas do alfabeto. Nas próximas M linhas há a informação dos jogos na seguinte forma: X timeA Y timeB, indicando que o timeA jogou contra o timeB e o primeiro marcou X gols e o segundo Y gols. As strings terão tamanho entre 1 e 20 e o número de gols de um time em cada partida será entre 0 e 100.Um time nunca joga contra ele mesmo, porém ele pode jogar inúmeras vezes contra qualquer outro time.

* ocorrerá em aproximadamente 90% dos casos de teste;
** ocorrerá no restante dos casos.

Saída
Imprima na ordem de classificação os times da entrada, um time em cada linha. Não é necessário imprimir nada entre os casos de teste!

Exemplo de Entrada	

3 #significa 3 testes

2 2 #1º teste, significa 2 times 2 jogos
palmeiras
santos
1 palmeiras 2 santos
2 palmeiras 0 santos

2 2 #2º teste, significa 2 times 2 jogos 
b
a
1 a 1 b
1 b 1 a

4 7 #3º teste, significa 4 times 7 jogos

b
a
c
d
2 a 1 b
1 b 1 a
2 c 3 a
4 b 2 d
0 b 1 c
1 b 0 c
7 d 1 b


Exemplo de saída
palmeiras
santos

b
a

b
a
d
c
'''
