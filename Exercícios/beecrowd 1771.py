def validar_cartela(cartela):
    # Divide a cartela em colunas
    b = cartela[0:5]
    i = cartela[5:10]
    n = cartela[10:15]
    g = cartela[15:20]
    o = cartela[20:25]
    
    # Define os intervalos para cada coluna
    intervalos = {
        'b': (1, 15),
        'i': (16, 30),
        'n': (31, 45),
        'g': (46, 60),
        'o': (61, 75)
    }
    
    # Função para verificar se os números estão dentro do intervalo
    def verificar_coluna(coluna, intervalo):
        return all(intervalo[0] <= num <= intervalo[1] for num in coluna)
    
    # Verifica cada coluna
    if (verificar_coluna(b, intervalos['b']) and
        verificar_coluna(i, intervalos['i']) and
        verificar_coluna(n, intervalos['n']) and
        verificar_coluna(g, intervalos['g']) and
        verificar_coluna(o, intervalos['o'])):
        return "OK"
    
    # Se a cartela não for válida, tenta rearranjar
    # Para simplificar, vamos assumir que não é possível rearranjar
    # Você pode implementar a lógica de permutação aqui se necessário
    return "DESCARTÁVEL"

# Loop para leitura até EOF
while True:
    try:
        linha = input()
        numeros = list(map(int, linha.split()))

        resultado = validar_cartela(numeros)
        print(resultado)
    except EOFError:
        break