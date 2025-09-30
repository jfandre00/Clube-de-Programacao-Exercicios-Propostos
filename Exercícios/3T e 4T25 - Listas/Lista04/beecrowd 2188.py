# Começamos numerando os testes
teste = 1

# Laço principal para processar todos os conjuntos de retângulos
while True:
    # Lemos o número de retângulos do conjunto
    N = int(input())
    
    # Se N = 0, significa que acabou a entrada
    if N == 0:
        break

    # Inicializamos a interseção com valores extremos
    # Esses valores garantem que o primeiro retângulo que processarmos
    # vai definir a interseção inicial corretamente
    x1, y1 = -10000, 10000  # canto superior esquerdo da interseção
    x2, y2 = 10000, -10000  # canto inferior direito da interseção

    # Processamos cada retângulo do conjunto
    for _ in range(N):
        # Leitura do retângulo: X,Y = canto superior esquerdo, U,V = canto inferior direito
        X, Y, U, V = map(int, input().split())
        
        # Atualizamos a interseção de todos os retângulos lidos até agora
        # Para o canto superior esquerdo da interseção:
        x1 = max(x1, X)  # pegamos o maior X inicial
        y1 = min(y1, Y)  # pegamos o menor Y inicial (mais para baixo)
        
        # Para o canto inferior direito da interseção:
        x2 = min(x2, U)  # pegamos o menor X final
        y2 = max(y2, V)  # pegamos o maior Y final (mais para cima)
    
    # Agora x1, y1, x2, y2 representam a interseção final
    # No final da 1ª leitura x1,x2,y1,y2 vai ser o 1º retângulo
    # Conforme vamos lendo, ele vai encontrando a interseção
    # cercando a área. Vai sobrando a área de interseção somente
    
    # Precisamos verificar se existe de fato
    print(f"Teste {teste}")  # identificador do teste
    
    # Condição de existência do retângulo de interseção:
    # Para existir, o canto superior esquerdo deve estar "acima e à esquerda" do canto inferior direito
    
    if x1 < x2 and y2 < y1:
        # Existe interseção: imprimimos no mesmo formato da entrada
        print(f"{x1} {y1} {x2} {y2}")
    else:
        # Não existe interseção
        print("nenhum")
    
    print()  # linha em branco entre os testes
    teste += 1  # incrementa o número do teste