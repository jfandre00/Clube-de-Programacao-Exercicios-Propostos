ENTRADAS = 5
contador = 0
for _ in range(ENTRADAS):
    numero = int(input())
    if numero % 2 == 0:
        contador += 1
        
print(f"{contador} valores pares")