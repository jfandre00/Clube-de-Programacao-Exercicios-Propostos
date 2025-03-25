# primeira linha contem N e W representando quantos titãs a tropa conhece e o tamanho da muralha que vão construir

# n linhas seguintes contem uma string S representando o nome do titã, seguida por um inteiro H representando a altura do titã. A string é compostas por letras maísculas, minúsculas e espaços, e tem no máximo 100 caracteres. A altura do titã é um inteiro entre 1 e 1000.
# o nome do titã nunca começa ou termina com espaço.

# devemos exibir quais titãs conseguem passar por cima da muralha, exibidos na ordem que foram informados


n, w = map(int, input().split())


for _ in range(n):
    linha = input().rsplit(' ', 1) # Separa o nome da altura
    
    nome = linha[0]  # Nome 
    h = int(linha[1])  # Altura
    
    # Se for maior que a largura, ele passa
    if h > w:
        print(nome)
