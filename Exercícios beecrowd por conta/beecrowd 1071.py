#beecrowd 1071 - Soma de Impares Consecutivos I

x = int(input())
y = int(input())

soma = 0

if x > y:
    x, y = y, x
for i in range(x+1, y):
    #print(i, end=' ')
    if i % 2 != 0:
        soma += i

print(soma)





