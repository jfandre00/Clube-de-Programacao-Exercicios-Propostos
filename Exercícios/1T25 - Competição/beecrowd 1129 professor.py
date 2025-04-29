#Leitura Ótica

# em cada prova, cada questão terá A B C D E como alternativas
# tons de cinza entre 0 (preto total) e 255 (branco total)
# (255, 0 , 255, 255, 255) seria alternativa B
# os valores podem ser menores que 255. Os quadrados serão classificados: Se a média for menor ou igual a 127 será preto e se for maior que 127 será branco.

alternativas = 'ABCDE'

n = int(input())
while n != 0:
    for _ in range(n):
        linha = input().split()
        alternativas_marcadas = [i for i in range(5) if int(linha[i]) <= 127]
        # para cada valor na linha, se o valor for menor ou igual a 127, adiciona o índice na lista alternativas_marcadas. índice 0 vai ser alternativa A, índice 1 vai ser alternativa B, etc.
        # se houver mais de uma alternativa marcada, a resposta é '*'
        # se houver apenas uma alternativa marcada, a resposta é a alternativa correspondente ao índice da lista alternativas_marcadas.
        if len(alternativas_marcadas) == 1:
            print(alternativas[alternativas_marcadas[0]])
        else:
            print('*')
    n = int(input()) # lê o próximo número de provas
# o loop continua até que n seja 0, que é o sinal de parada do programa.