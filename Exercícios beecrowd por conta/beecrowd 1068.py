#beecrowd | 1068 - Balanço de Parênteses

while True:
    try:
        expressao = input()
        #removendo tudo da string exceto ( e )
        expressao = ''.join([c for c in expressao if c in '()'])
        if expressao == '':
            print('correct')
        elif expressao[0] == ')' or expressao[-1] == '(':
            print('incorrect')
        else:
            if len(expressao) % 2 == 0:
                print('correct')
            else:
                print('incorrect')
    except EOFError:
        break