#beecrowd 2866

#Pode-se notar que o padrão é remover as letras maiúsculas e inverter as minúsculas.

C = int(input())
lista = []
for i in range(0, C):
    criptotexto = input()
    lista.append(criptotexto)

i = 0
while i < len(lista): #Rodar a lista item por item
    strTeste = lista[i] 
    resultado = ''.join(filter(str.islower, strTeste)) # Usando o método filter e str.islower
    palavra_correta = resultado[::-1] #invertendo a palavra
    print(palavra_correta)
    i += 1

'''
Enunciado:
César é um detetive que investiga uma série de roubos que acontecem em sua cidade. Em todo lugar que um crime acontece, a pessoa que cometeu tal crime deixa uma mensagem escrita, formada por letras maiúsculas e minúsculas. César conseguiu achar um padrão nestas mensagens e agora extrai um texto oculto em cada mensagem e pede a sua ajuda para tentar descobrir quem está cometendo tais crimes.

Entrada
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro C (2 <= C <= 99) relativo ao número de casos de teste. Nas C linhas seguintes, haverá mensagens codificadas, todas com um mesmo padrão em relação ao exemplo abaixo.

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir o texto extraído da mensagem original.

Exemplo de Entrada	
3
NoTApasCAL
atEQUEatabELATERMINE
zoEIrrRRRRa
Exemplo de Saída
sapo
batata
arroz
'''
