def formatacaoMatriz(matriz):
    
    comprimentoColunas = [max(len(str(matriz[i][j])) for i in range(len(matriz))) for j in range(len(matriz))]
       
    linhasFormatadas = [] #criando a matriz formatada
    for linha in matriz:
        print(linha)
        linha_a_formatar = ' '.join(f'{valor:>{comprimentoColunas[j]}}' for j, valor in enumerate(linha))
        #dá um espaco e junta com a f string. para alinhar a string valor é alinhada a direita
        linhasFormatadas.append(linha_a_formatar)
        
    return ''.join(linhasFormatadas) #já retorna quebrando as linhas


print(formatacaoMatriz([[100,2,3], [4,50,6], [7,8,9000]]))

