'''notas_100 = dinheiro // 100
dinheiro -= (notas_100*100)
notas_50 = dinheiro // 50
dinheiro -= (notas_50*50)
notas_20 = dinheiro // 20
dinheiro -= (notas_20*20)
notas_10 = dinheiro // 10
dinheiro -= (notas_10*10)
notas_5 = dinheiro // 5
dinheiro -= (notas_5*5)
notas_2 = dinheiro // 2
dinheiro -= (notas_2*2)

moedas_1 = dinheiro // 1
dinheiro -= (moedas_1*1)

moedas_50 = dinheiro // 0.50
dinheiro -= (moedas_50*0.5)'''

def calculo_dinheiro_moeda(dinheiro, cedula):
    notas = dinheiro // cedula
    dinheiro -= (notas*cedula)
    resposta.append(notas)
    return dinheiro

resposta = []
cedulas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]

dinheiro = float(input())

for c in range(len(cedulas)):
    dinheiro = calculo_dinheiro_moeda(dinheiro, cedulas[c])

for m in range(len(resposta)):
    if m == 0:
        print("NOTAS:")
    if m == 6:
        print("MOEDAS:")
    if m in range(0,6):
        print(f'{resposta[m]:.0f} nota(s) de R$ {cedulas[m]:.2f}')
    if m in range(6,12):
        print(f'{resposta[m]:.0f} moeda(s) de R$ {cedulas[m]:.2f}')
