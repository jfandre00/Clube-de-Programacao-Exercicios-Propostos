#Pão a metro - beecrowd 2329

#N pessoas e K sanduíches, com metros de pão M1, M2, M3, ..., MK
#Exemplo: K = 4 -> M1 = 120, M2 = 89, M3 = 230 e M4 = 177 e N = 10
#Teríamos N fatias iguais de tamanho máximo 57, pois assim teríamos 2 fatias no M1
#1 fatia no M2, 4 fatias no M3 e 3 fatias no M4 - totalizando 10 fatias

#Qual o tamanho inteiro máximo de fatia que pode ser cortada de modo que cada pessoa receba pelo menos uma fatia?


###############################################
#Qual é o essencial para resolver o problema?#
#Queremos encontrar o maior valor de fatia possível
#Fazer uma busca por um valor que atenda as nossas restrições
#Definir quais são os limites máximos e mínimos que são viáveis para a solução do problema
#O mínimo que a fatia pode ter é 1 cm e o máximo é a soma de todos os tamanhos de pão dividido pela 
#quantidade de pessoas. Assim teremos uma estimativa inicial de qual é o tamanho máximo de fatia que podemos ter
###########################################

#1. calcula o maior tamanho de fatia possível
# tamanho_máximo = 120 + 89 + 230 + 177 = 616
# 616 // 10 = 61
#Contar quantas fatias de tamanho 61 podemos ter
#120 // 61 = 1
#89 // 61 = 1
#230 // 61 = 3
#177 // 61 = 2
#Total = 7 -> se fosse maior ou igual a 10, ok, se não, diminui o tamanho da fatia. 
#2. diminui o tamanho da fatia (t-1) e repete o processo
#60
#120 // 60 = 2
#89 // 60 = 1
#230 // 60 = 3
#177 // 60 = 2
#Total = 8 -> se fosse maior ou igual a 10, ok, se não, diminui o tamanho da fatia.
#3. diminui o tamanho da fatia (t-1) e repete o processo
#59
#120 // 59 = 2
#89 // 59 = 1
#230 // 59 = 3
#177 // 59 = 2
#Total = 8 -> se fosse maior ou igual a 10, ok, se não, diminui o tamanho da fatia.
#4. diminui o tamanho da fatia (t-1) e repete o processo
#58
#120 // 58 = 2
#89 // 58 = 1
#230 // 58 = 3
#177 // 58 = 3
#Total = 9 -> se fosse maior ou igual a 10, ok, se não, diminui o tamanho da fatia.
#5. diminui o tamanho da fatia (t-1) e repete o processo
#57
#120 // 57 = 2
#89 // 57 = 1
#230 // 57 = 4
#177 // 57 = 3
#Total = 10 -> se fosse maior ou igual a 10, ok, se não, diminui o tamanho da fatia.
#Portanto, o tamanho máximo de fatia que podemos ter é 57

n = int(input())
k = int(input())
m = [int(x) for x in input().split()]


#Algoritmo 1
#Calcula maior tamanho de fatia possível
tmax = sum(m) // n

#Para cada tamanho possível...
for t in range(1, tmax+1):
    #Calcula o máximo de fatias com tamanho t
    fatias = 0
    for i in range(k):
        fatias += m[i] // t

    #Se o número de fatias for menor que o de pessoas, a solução é t-1
    if fatias < n:
        print(t-1)
        break

#Qual a eficiência do algoritmo feito acima?
#O algoritmo acima tem complexidade O(n*k), pois para cada tamanho de fatia possível, ele percorre todos os pães -> percorre todos os pães para cada tamanho de fatia (busca linear)

#Algoritmo 2 - busca binária

#Vamos olhar o elemento do meio para saber se ele é maior ou menor que o número de fatias que precisamos
#Se for maior, vamos para a esquerda, se for menor, vamos para a direita
#Em uma verificação, já descartamos metade dos elementos
#Os limites mínimo e máximo vão mudando conforme vamos fazendo as verificações e mudando o meio

#Continuar buscando enquanto eu tiver o limite inferior for menor ao limite superior

#Solução:

n = int(input())
k = int(input())
m = [int(x) for x in input().split()]

#Define o menor e o maior tamanhos de fatia possíveis
tmin = 1
tmax = sum(m) // n

#Faz uma busca binária
while tmin < tmax:
    #Calcula o tamanho médio dentro da faixa considerada
    t = (tmin + tmax + 1) // 2

    #Calcula o máximo de fatias com tamanho t
    fatias = 0
    for i in range(k):
        fatias += m[i] // t
    
    #Atualiza os limites de tamanho de fatia
    if fatias < n:
        tmax = t - 1
    else:
        tmin = t

#A solução é o tmin
print(tmin)














