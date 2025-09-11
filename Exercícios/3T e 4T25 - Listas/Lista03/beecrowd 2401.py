#Calculadora

# máquinas que fazem apenas operações de multiplicação e divisão
# a calculadora sempre começa com o valor 1

quantidade_de_operacoes = int(input())
resultado = 1
for _ in range(quantidade_de_operacoes):
    valor, operacao = input().split()
    valor = int(valor)
    if operacao == '*':
        resultado *= valor
    elif operacao == '/':
        resultado /= valor

print(f"{resultado:.0f}") #ou usar o round(resultado) para arredondar o resultado