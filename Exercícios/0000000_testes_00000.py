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


times = ["palmeiras", "corinthians", "santos", "vasco"]

resultados = [
    "2 corinthians 2 palmeiras",
    "1 corinthians 1 palmeiras",
    "3 palmeiras 2 corinthians",
    "3 corinthians 0 vasco",
    "3 santos 1 vasco",
    "3 vasco 1 palmeiras",
    "3 corinthians 1 vasco",
    "4 palmeiras 2 vasco"

]

# Inicializar dicionário para armazenar pontos, gols e posição
dados = {time: {"pontos": 0, "gols": 0, "posicao": i} for i, time in enumerate(times)}

# Função para determinar o vencedor, atualizar os pontos e somar os gols
def atualizar_dados(resultados, times, dados):
    for resultado in resultados:
        partes = resultado.split()  # Dividir a string em partes
        gols_time1 = int(partes[0])
        nome_time1 = partes[1]
        gols_time2 = int(partes[2])
        nome_time2 = partes[3]
        
        # Atualizar gols
        dados[nome_time1]["gols"] += gols_time1
        dados[nome_time2]["gols"] += gols_time2
        
        # Atualizar pontos
        if gols_time1 > gols_time2:
            dados[nome_time1]["pontos"] += 3  # Time1 vence
        elif gols_time1 < gols_time2:
            dados[nome_time2]["pontos"] += 3  # Time2 vence
        else:
            dados[nome_time1]["pontos"] += 1  # Empate
            dados[nome_time2]["pontos"] += 1

# Atualizar os dados com base nos resultados
atualizar_dados(resultados, times, dados)

# Ordenar os times primeiro pelos pontos (em ordem decrescente), depois pelos gols (em ordem decrescente) e finalmente pela posição original (em ordem crescente)
times_ordenados = sorted(dados.items(), key=lambda item: (-item[1]['pontos'], -item[1]['gols'], item[1]['posicao']))

# Exibir os pontos, gols e posição finais
for time, stats in times_ordenados:
    print(f"{time}: {stats['pontos']} pontos, {stats['gols']} gols, posição original {stats['posicao']}")
