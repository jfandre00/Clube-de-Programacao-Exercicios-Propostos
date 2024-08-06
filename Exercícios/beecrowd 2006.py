T = int(input())
entrada = list(map(int, input().split()))
saida = 0

for e in entrada:
    if e == T:
        saida += 1
        
print(saida)