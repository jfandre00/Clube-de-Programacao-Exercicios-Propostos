O = input().strip()  # 'S' ou 'M' soma ou média
total = 0.0
count = 0

# vamos ler a matriz
for i in range(12):
    for j in range(12):
        x = float(input()) #vai lendo todas as entradas
        # conforme vou lendo as entradas já irei testando 
        if j > i:  # está acima da diagonal principal M[i,j] 
            total += x
            count += 1

if O == 'S':
    resultado = total
else: # é M
    resultado = total / count

print(f"{resultado:.1f}")