teclado = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ' '
}

entradas = int(input())
for _ in range(entradas):
    mensagem = input()
    resultado = ''
    ultima_tecla = None  # P/ saber se precisamos colocar '*'
    
    for letra in mensagem:
        # Verificando maiúsculas
        if letra.isupper():
            resultado += '#'
        
        # Descobrir a tecla da letra atual
        tecla_atual = None
        for tecla, letras in teclado.items():
            if letra.lower() in letras:
                tecla_atual = tecla
                press = str(tecla) * (letras.index(letra.lower()) + 1)
                break
        
        # Se a tecla atual for a mesma da última e a última letra NÃO foi maiúscula
        # precisamos colocar '*'
        if ultima_tecla == tecla_atual and not letra.isupper() and resultado[-1] != '#':
            resultado += '*'
        
        resultado += press
        ultima_tecla = tecla_atual
    
    print(resultado)

        
