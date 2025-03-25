# beecrowd 1129

while True:
    n = int(input())
    if n == 0:
        break
    
    opcoes = "ABCDE"
    
    for _ in range(n):
        valores = list(map(int, input().split()))
        
        # maior que 127 é marcado
        marcados = [i for i, valor in enumerate(valores) if valor <= 127]
        
        # confirmar se há apenas um marcado
        if len(marcados) == 1:
            resposta = opcoes[marcados[0]]  
        else:
            resposta = '*'
        
        print(resposta)

