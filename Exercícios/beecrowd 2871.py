while True:
    try:
        m, n = map(int, input().split())
        soma_cafe = 0

        for i in range(m):
            matriz = list(map(int, input().split()))
            soma_cafe += sum(matriz)
            
        saca = soma_cafe // 60
        litro = soma_cafe % 60

        print(f'{saca} saca(s) e {litro} litro(s)')
    except EOFError:
        break

