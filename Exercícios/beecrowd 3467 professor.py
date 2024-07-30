'''
A entrada termina com EOF - estrutura while true com try except - consultar material no moodle da disciplina.
'''

while True:
    try:
        sofa = input()
        if sofa[2] == 'L':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break

