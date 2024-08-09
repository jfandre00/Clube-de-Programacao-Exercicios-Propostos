from itertools import permutations

def verificar_intervalos(coluna, intervalo):
    return all(intervalo[0] <= x <= intervalo[1] for x in coluna)

def processar_cartela(numeros):
    # Inserir 0 na posição 12 para ter 25 elementos
    numeros.insert(12, 0)
    
    # Separar números em cinco categorias
    B = numeros[0:5]
    I = numeros[5:10]
    N = numeros[10:15]
    G = numeros[15:20]
    O = numeros[20:25]
    
    # Remover o zero
    N.remove(0)
    
    # Definir intervalos para cada coluna
    intervalos = {
        'B': (1, 15),
        'I': (16, 30),
        'N': (31, 45),
        'G': (46, 60),
        'O': (61, 75)
    }
    
    # Verificar se todos os números estão dentro dos intervalos
    intervalo_B = verificar_intervalos(B, intervalos['B'])
    intervalo_I = verificar_intervalos(I, intervalos['I'])
    intervalo_N = verificar_intervalos(N, intervalos['N'])
    intervalo_G = verificar_intervalos(G, intervalos['G'])
    intervalo_O = verificar_intervalos(O, intervalos['O'])
    
    if intervalo_B and intervalo_I and intervalo_N and intervalo_G and intervalo_O:
        return "OK"
    
    # Verificar permutações
    for perm in permutations(numeros):
        B_perm = perm[0:5]
        I_perm = perm[5:10]
        N_perm = perm[10:15]
        G_perm = perm[15:20]
        O_perm = perm[20:25]
        
        if (verificar_intervalos(B_perm, intervalos['B']) and
            verificar_intervalos(I_perm, intervalos['I']) and
            verificar_intervalos(N_perm, intervalos['N']) and
            verificar_intervalos(G_perm, intervalos['G']) and
            verificar_intervalos(O_perm, intervalos['O'])):
            return "RECICLAVEL"
    
    return "DESCARTAVEL"

while True:
    try:
        numeros = list(map(int, input().split()))
        
        resultado = processar_cartela(numeros)
        print(resultado)
    
    except EOFError:
        break