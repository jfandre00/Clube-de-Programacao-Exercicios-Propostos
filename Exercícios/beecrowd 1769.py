def verificadorCPF(nCPF, b):
    total = 0
    n = 1
    for i in range(0,9):
        total += int(nCPF[i])*n
        n += 1

    verificador = total % 11
    if verificador == 10:
        verificador = 0
    
    if verificador == int(b):
        return True
    else:
        return False

'''
Tive erro de runtime porque tinha feito com while < 10000 que foi o numero máximo de inserções no exercício, mas na verdade deveria ter usado o while True mesmo
'''

try:

    while True:
        cpf = input()

        cpf_sem_pontos = cpf.replace(".","")
        cpf_limpo = cpf_sem_pontos.replace("-","")

        todos_a_b1 = cpf_limpo[0:9]
        todos_a_b2 = todos_a_b1[::-1]
        b1 = cpf_limpo[-2]
        b2 = cpf_limpo[-1]

        teste_b1 = verificadorCPF(todos_a_b1,b1)
        teste_b2 = verificadorCPF(todos_a_b2,b2)

        if (teste_b1 and teste_b2) == True:
            print("CPF valido")
        else:
            print("CPF invalido")
except EOFError:
    pass
