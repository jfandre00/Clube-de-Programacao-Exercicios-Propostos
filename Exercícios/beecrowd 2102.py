def processar_instancias():
    T = int(input().strip()) #T é o número de instâncias
    
    for instancia in range(1, T+1):
        N, L = map(int, input().strip().split()) #N é a dimensão da matriz, L são entradas não nulas
        
        matriz_soma = {}
        
        for _ in range(L):
            Pk, lk, ck, vk =map(int, input().strip().split()) #Pk - nº da matriz que estou adicionando
                                                              #lk - linha aonde vk está
                                                              #ck - coluna aonde vk está
                                                              #vk é o valor na posição (lk,ck) na matriz Pk
            
            if (lk, ck) not in matriz_soma:
                matriz_soma[(lk, ck)] = 0
            matriz_soma[(lk, ck)] += vk
            
        nao_nulos = sorted(matriz_soma.items())
        
        if instancia > 1:
            print()
            
        for (lk, ck), vk in nao_nulos:
            print(lk, ck, vk)

processar_instancias()

'''
Por exemplo para uma entrada : 1 instancia / matriz de ordem 3 e 3 valores 
entradas dos valores : 1 0 1 10 (primeira matriz na posicao (0,1) o valor é 10)
                       1 1 2 5 (primeira matriz na posição (1,2) o valor é 5)
                       1 1 2 15 (primeira matriz na posição (1,2) o valor é 15)
na saída então teremos - 0 1 10 (posição (0,1) resultou o valor 10)
(1 2 20) posição (1,2) resultou o valor 20

2º exemplo: 
entro com 2 / 2 2 (2 instancias) / (a primeira tem ordem 2 e 2 valores)
1 0 0 3 (matriz 1 na posicao 0,0 o valor é 3)
1 1 1 4 (matriz 1 na posição 1,1 o valor é 4)
3 3 (a segunda entrada tem ordem 3 e 3 valores)
1 0 2 7 (matriz 1 na posicao 0,2 o valor é 7)
1 2 1 1 (matriz 1 na posição 2,1 o valor é 1)
2 0 2 3 (matriz 2 na posição 0,2 o valor é 3)
a saída deverá ser:
0 0 3 (na posicao 0,0 temos 3)
1 1 4 (na posicao 1,1 temos 4)

0 2 10 (na posicao 0,2 temos 10, que no caso é a soma do 7 com o 3 acima)
2 1 1 (na posição 2,1 temos 1)
'''