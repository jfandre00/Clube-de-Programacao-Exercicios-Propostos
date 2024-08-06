N = int(input())
contador = 1

while contador <= N:
    print(f'{contador} {contador**2} {contador**3}')
    print(f'{contador} {(contador**2)+1} {(contador**3)+1}')
    contador += 1