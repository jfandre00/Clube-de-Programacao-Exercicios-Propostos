'''n = int(input())
divisores = []
divisores_maior = []
duendes = list(map(int, input().split()))

for i in range(len(duendes)):
    for j in range(1, duendes[i] + 1):
        if duendes[i] % j == 0 and j not in divisores:
            divisores.append(j)

divisores.sort()

maior_numero = divisores[-1]

for i in range(len(divisores)):
    if maior_numero % divisores[i] == 0:
        maior_numero += 1
        continue

print(maior_numero)'''
        
    
### Solução aceita bem mais simples

n = int(input())
duendes = list(map(int, input().split()))
maior = max(duendes) 
res = maior + 1 # começa a busca a partir do maior número da lista

while True:
    if all(d % res != 0 for d in duendes): # verifica se é divisível por algum dos duendes. Se for, continua a busca
        print(res)
        break
    res += 1
        
            