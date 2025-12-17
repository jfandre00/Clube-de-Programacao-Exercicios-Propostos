# 1. Leia a operação (S para Soma, M para Média)
operacao = input()

soma = 0.0
contador = 0

# 2. Use dois loops para simular as posições [linha][coluna]
for linha in range(12):
    for coluna in range(12):
        
        # 3. LEIA o número. Temos que ler todos, mesmo os que não vamos usar.
        numero = float(input())
        
        # 4. Verifique se a Posição [linha][coluna] está na área esquerda
        # A condição é: coluna < linha E coluna < (11 - linha)
        if coluna < linha and coluna < (11 - linha):
            soma += numero
            contador += 1 # Este contador vai chegar a 30

# 5. Imprima o resultado com base na operação
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    # Sabemos que o contador é 30, então podemos dividir por 30.0
    media = soma / 30.0
    print(f"{media:.1f}")