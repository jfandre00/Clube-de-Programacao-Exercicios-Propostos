'''def formatacaoMatriz(matriz):
    
    comprimentoColunas = [max(len(str(matriz[i][j])) for i in range(len(matriz))) for j in range(len(matriz))]
       
    linhasFormatadas = [] #criando a matriz formatada
    for linha in matriz:
        print(linha)
        linha_a_formatar = ' '.join(f'{valor:>{comprimentoColunas[j]}}' for j, valor in enumerate(linha))
        #dá um espaco e junta com a f string. para alinhar a string valor é alinhada a direita
        linhasFormatadas.append(linha_a_formatar)
        
    return ''.join(linhasFormatadas) #já retorna quebrando as linhas


print(formatacaoMatriz([[100,2,3], [4,50,6], [7,8,9000]]))'''

def atualizar_dados(resultados, pontos):
    for resultado in resultados:
        partes = resultado.split()
        gols_time1 = int(partes[0])
        nome_time1 = partes[1]
        gols_time2 = int(partes[2])
        nome_time2 = partes[3]

        #Atualizar gols
        dados[nome_time1]['gols'] += gols_time1
        dados[nome_time2]['gols'] += gols_time2

        #Atualizar pontos
        if gols_time1 > gols_time2:
            dados[nome_time1]['pontos'] += 3
        elif gols_time1 < gols_time2:
            dados[nome_time2]['pontos'] += 3
        else:
            dados[nome_time1]['pontos'] += 1
            dados[nome_time2]['pontos'] += 1



times = ["palmeiras", "corinthians", "santos", "vasco"]

resultados = [
    "2 corinthians 2 palmeiras",
    "1 corinthians 1 palmeiras",
    "3 palmeiras 2 corinthians",
    "3 corinthians 0 vasco",
    "3 santos 1 vasco",
    "3 vasco 1 palmeiras"

]
#Dicionário de dados
dados = {time: {'pontos': 0, 'gols': 0, 'posicao': times.index(time)} for time in times}

atualizar_dados(resultados, dados)

#Ordenar os times com base nos pontos e na posição como critério de desempate
times_ordenados = sorted(dados.items(), key=lambda item: (-item[1]['pontos'], item[1]['posicao']))

#Exibir os pontos, gols e posição final
for time, info in times_ordenados:
    print(f"{time}: {info['pontos']} pontos, {info['gols']} gols, posição original {info['posicao']}")

