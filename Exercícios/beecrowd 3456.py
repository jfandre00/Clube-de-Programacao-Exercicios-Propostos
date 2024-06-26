#beecrowd 3456


#Lê o numero como string, removendo espaços em branco extras.
X = input().strip()

#Conversão Incial
C = int(X)
print(X)

#Loop de transformação: Continua enquanto C tiver mais de um dígito
while C > 9:
    #Extrair os dígitos exceto o último
    parte_esquerda = X[:-1]
    ultimo_digito = X[-1]

    #Calcular a nova palavra de acordo com a regra da divisibilidade por 7.
    nova_palavra = int(parte_esquerda) * 3 + int(ultimo_digito)

    #Atualizar X e C para a próxima iteração
    X = str(nova_palavra)
    C = nova_palavra

    print(X)

#As linhas abaixo não foram aceitas pelo beecrowd, mas faz sentido ter para entendimento do problema
#Verificação final
if C % 7 == 0:
    print(f"O número é divisível por 7.")
else:
    print(f"O número não é divisível por 7.")