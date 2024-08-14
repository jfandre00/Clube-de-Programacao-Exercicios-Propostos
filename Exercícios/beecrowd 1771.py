#beecrowd 1771

#coluna letra B faixa 1 a 15, I 16 a 30, N 31 a 45, G 46 a 60, O 61 a 75

#OK se a cartela for válida / Reciclavel se houver permutação possível /Descartavel se não existir permutação

#1. verificar se está ok
#2. se não, como verificar se é possível transformar uma cartela em reciclável?

#Verificar a quantidade de números que estão em cada letra, e ver se para cada letra tinha 5 numeros B I N G O
#temos que ter 4 na faixa N - para resolver isso colocamos o elemento extra na lista
#contamos quantos valores tem em cada faixa, e se tem exatamente essas quantidades de valores podemos transformar em reciclável

while True:
    try:
        cartela = list(map(int, input().split()))
        cartela.insert(12, 43) #Inserindo nessa posição que é aonde está o índio, qualquer número N entre 31 e 45
        ok = True
        for coluna in range(5): #indice inicial 0,1,2,3,4 (B I N G O)
            for i in range(coluna, len(cartela), 5): #pula de 5 em 5, pega os valores B I N G O
                if (cartela[i] - 1) // 15 != coluna: #se o intervalo é coluna B - essa conta tem que dar zero, no I tem que dar 1 e assim por diante (um número entre 1 e 15 dividido por 15 - 1 vai ser zero)
                    ok = False
                    break
        if ok:
            print("OK")  #não encontrou nada fora do lugar, então está ok
        else:
            contador = [0] * 5  #lista para armazenar os contadores, para ser reciclável tem que ter 5 elementos em cada, tornando possível a permutação
            recicla = True
            for numero in cartela:
                coluna = (numero - 1) // 15
                contador[coluna] += 1
                if contador[coluna] > 5:
                    recicla = False
                    break
            if recicla:
                print("RECICLAVEL")
            else:
                print("DESCARTAVEL")
    except EOFError:
        break
        