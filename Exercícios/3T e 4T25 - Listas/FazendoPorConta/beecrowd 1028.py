'''n = int(input())


for _ in range(n):

    f1, f2 = map(int, input().split())

    menor = min(f1, f2)
    divisores_f1 = []
    divisores_f2 = []

    for i in range(1, menor + 1):
        if f1 % i == 0:
            divisores_f1.append(i)
        if f2 % i == 0:
            divisores_f2.append(i)

    divisores_f1.sort()
    divisores_f2.sort()

    tamanho_f1 = len(divisores_f1)
    tamanho_f2 = len(divisores_f2)

    if tamanho_f1 >= tamanho_f2:
        for i in range(tamanho_f2 - 1, -1, -1):
            if divisores_f1[i] in divisores_f2:
                print(divisores_f1[i])
                break
    else:
        for i in range(tamanho_f1 - 1, -1, -1):
            if divisores_f2[i] in divisores_f1:
                print(divisores_f2[i])
                break'''

n = int(input())

def gcd(a, b): # Função para calcular o MDC usando o Algoritmo de Euclides
    while b: # Enquanto b for diferente de zero
        a, b = b, a % b # Atribui a b o valor de a % b
    return a 

for _ in range(n):
    f1, f2 = map(int, input().split())
    print(gcd(f1, f2))