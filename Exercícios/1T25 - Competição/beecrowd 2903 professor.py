#Algoritmo - primeira coisa é saber quantas voltas eu preciso dar na pizza considerando giros igual a R (angulo do teste). Inicialmente será 1 volta
# Enquanto (voltas * 360) não for divisível por R, eu vou somando 1 na variável voltas
# Depois que eu sair do laço, eu vou calcular o número de fatias iguais, que é voltas * 360 / R

#as entradas tem exatamente 2 casas decimais, então eu posso multiplicar por 100 e fazer a divisão inteira

r = float(input())
r = int(r * 100)
voltas = 1
while (voltas * 36000) % r != 0:
    voltas += 1
fatias = (voltas * 36000) // r

print(fatias)
