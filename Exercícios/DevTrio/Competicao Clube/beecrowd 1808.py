#cada nota inteiro entre 1 e 10
'''
O profílico autor Stephen King estava entrando com as notas dos seus estudantes de literatura numa calculadora geral de médias on-line. Quando terminou, ele percebeu que sua tecla de retorno (ENTER) estava quebrada. Então, ao invés de entrar com as notas de um estudante numa linha separada cada, ele entrou com elas numa única linha sem separação alguma. Uma vez que o Sr. King não possui as habilidades para consertar sua tecla de retorno, ele precisa que você calcule a média das notas dos estudantes a partir da entrada não separada.

Cada nota é um inteiro entre 1 e 10. Todas as notas foram digitadas na base 10 sem zeros à esquerda. Por exemplo, se as notas do estudante do Sr. King foram 3, 10, 1 e 10, elas seriam entradas com “310110”.

Entrada
A entrada consiste de uma única linha que contém uma cadeia de caracteres não-vazia S de no máximo 100 dígitos na base 10. Há uma única maneira de particionar S numa lista de subcadeias de caracteres de tal modo que cada subcadeia represente um inteiro entre 1 e 10 na base 10 sem zeros à esquerda.

Saída
Imprima uma linha com um número racional representando a média das notas do estudante cujas notas o Sr. King entrou como S. O resultado deve ser impresso como um número racional, arredondado se necessário, com exatos dois dígitos depois do ponto decimal.
'''

#Solução

S = input().strip()  # Lê a string de entrada contendo as notas

notas = []
i = 0

# Percorre a string para identificar as notas
while i < len(S):
    if i < len(S) - 1 and S[i:i+2] == '10':
        notas.append(10)
        i += 2  # Avança dois caracteres, pois "10" tem dois dígitos
    else:
        notas.append(int(S[i]))
        i += 1  # Avança um caractere, pois números de 1 a 9 têm um dígito

# Calcula a média das notas
media = sum(notas) / len(notas)

# Imprime a média com dois dígitos decimais
print(f"{media:.2f}")