# Ler a quantidade de presentes
N = int(input())

# Inicializar a quantidade total de papel de embrulho necessário
total_papel = 0

# Processar cada presente
for p in range(N):
    # Ler as dimensões do presente no formato lxwxh
    l, w, h = map(int, input().split('x'))
    
    # Calcular a área das três faces
    lado1 = l * w
    lado2 = w * h
    lado3 = h * l
    
    # Calcular a área total de superfície
    area_superficie = (2 * lado1) + (2 * lado2) + (2 * lado3)
    
    # Calcular o papel extra necessário
    papel_extra = min(lado1, lado2, lado3)
    
    # Somar a quantidade total de papel necessário para este presente
    total_papel += area_superficie + papel_extra

# Imprimir a quantidade total de papel de embrulho necessário
print(total_papel)