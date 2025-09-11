'''
O número de regiões formadas por n retas em posição geral (ou seja, sem retas paralelas e com cada duas retas concorrentes em um ponto distinto) no plano é dado pela fórmula (n² + n + 2) / 2
'''

n = int(input())

for _ in range(n):
    retas = int(input())
    regioes = retas*((retas+1)/2) +1
    print(int(regioes))