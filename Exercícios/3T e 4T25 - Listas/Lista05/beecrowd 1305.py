import math

while True:
    try:
        # 1. Leia as duas linhas de entrada
        num_str = input()
        cutoff_str = input()
        
        # 2. Converta as strings em números (floats)
        num_float = float(num_str)
        valor_corte = float(cutoff_str)
        
        # 3. Separe o 'num' em parte inteira e fracionária
        
        # int() em um float "trunca" o número (joga fora o decimal).
        # Ex: int(3.65) se torna 3.
        # Ex: int(1.99) se torna 1.
        parte_inteira = int(num_float)
        
        # A parte fracionária é o número original menos a parte inteira
        # Ex: 3.65 - 3 = 0.65
        # Ex: 1.99 - 1 = 0.99
        parte_fracionaria = num_float - parte_inteira
        
        # 4. A Lógica de Arredondamento
        
        # (O problema garante que parte_fracionaria NUNCA será == valor_corte)
        
        if parte_fracionaria > valor_corte:
            # Se for maior, arredondamos para CIMA
            # (somamos 1 à parte inteira que já temos)
            print(parte_inteira + 1)
        else:
            # Se for menor, arredondamos para BAIXO
            # (simplesmente imprimimos a parte inteira truncada)
            print(parte_inteira)

    # 5. O loop para quando o Beecrowd para de enviar dados (EOF)    
    except EOFError:
        break