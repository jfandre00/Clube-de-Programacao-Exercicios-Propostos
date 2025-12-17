# O loop principal lê até encontrar o 0
while True:
    try:
        N = int(input())
        
        # 1. Condição de parada
        if N == 0:
            break
            
        # 2. Loop para as linhas (de 0 a N-1)
        for linha in range(N):
            
            # 3. Loop para as colunas (de 0 a N-1)
            for coluna in range(N):
                
                # 4. A Fórmula Mágica (lógica para calcular o valor)
                valor = abs(linha - coluna) + 1
                
                # 5. O Truque da Formatação
                if coluna == 0:
                    # Se for a primeira coluna, imprime o valor
                    # formatado para 3 dígitos, sem espaço antes.
                    print(f"{valor:3d}", end="")
                else:
                    # Para as outras colunas, imprime UM espaço
                    # e DEPOIS o valor formatado para 3 dígitos.
                    print(f" {valor:3d}", end="")
            
            # 6. Depois que todas as colunas da linha acabarem, pule a linha
            print()
        
        # 7. Depois que a matriz inteira acabar, pule uma linha em branco
        print()

    except EOFError:
        break