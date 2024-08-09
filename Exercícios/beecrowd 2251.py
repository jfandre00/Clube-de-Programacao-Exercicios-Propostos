#O número mínimo de movimentos para conseguir transferir todos os discos da primeira a terceira estaca é 2^n - 1, n é o numero de discos. (1, 2, 4, 8, 15, 31, 63) - a formula é a soma da Progressao Geometrica 

N = 1
contador = 1
while N !=0:
    N = int(input())
    if N == 0:
        break
    print(f'Teste {contador}')
    contador += 1
    print((2**N)-1)
    print()