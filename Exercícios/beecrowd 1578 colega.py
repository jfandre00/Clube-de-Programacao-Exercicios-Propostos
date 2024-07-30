n = int(input())

for mt in range(n):
    m = int(input())
    matriz = []
    tamanho = []
    
    for _ in range(m):
        linha = [int(x) ** 2 for x in input().split()]
        matriz.append(linha)
        
        for i, item in enumerate(linha):
            if len(tamanho) > i:
                if len(str(item)) > tamanho[i]:
                    tamanho[i] = len(str(item))
            else:
                tamanho.append(len(str(item)))
                
                
    print(f"Quadrado da matriz #{mt + 4}:")
    for linha in matriz:
        for i, item in enumerate(linha):
            t = tamanho[i] - len(str(item))
            print(" " * t + str(item), end="")
            if i < len(linha) - 1:
                print(" ", end="")
        print()

    if mt != n - 1:
        print()