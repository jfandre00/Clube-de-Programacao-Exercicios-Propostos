#Exercício 2144 Plataforma Timus Online Judge https://acm.timus.ru/problem.aspx?space=1&num=2144
#Enunciado do exercício abaixo

def le_caixas(n):
    caixas = []
    for _ in range(n):
        caixa = [int(c) for c in input().split()]
        caixa.pop(0)
        caixas.append(caixa)        
    return caixas

def todas_caixas_ok(caixas):
    return all(caixa_ok(caixa) for caixa in caixas)

def caixa_ok(caixa):
    return all(caixa[i] <= caixa[i+1] for i in range(len(caixa)-1))

def extremidades_caixas(caixas):
    return [[caixa[0], caixa[-1]] for caixa in caixas]

def extremidades_ok(extremidades):
    return all(extremidades[i][1] <= extremidades[i+1][0] for i in range(len(extremidades)-1))


# Leitura da entrada
n = int(input())
caixas = le_caixas(n)

# Verifica se todas as caixas estão OK
if not todas_caixas_ok(caixas):
    print('NO')
else:
    # Obtém nova lista de caixas só com as alturas das extremidades
    extremidades = extremidades_caixas(caixas)

    # Ordena caixas
    extremidades.sort()

    # Determina se as caixas estão organizadas
    if extremidades_ok(extremidades):
        print('YES')
    else:
        print('NO')


'''
Mom asked Lena to clean her room before she plays her favorite online game. Lena almost succeeded: she made the bed, put her clothes into the wardrobe and even threw out all the litter. The last chore remaining is to put all the boxes with action figures onto the shelves.
Lena has n boxes, numbered from 1 to n. Box number i contains ki action figures, each of its own size aij. Lena wants to finish quickly, but it’s very important to put all the figures in a non-decreasing order by their size. If it’s impossible, then the cleaning cannot be finished at all. Lena has quite a lot of boxes, so she isn’t sure if it can be done.
Lena values her boxes with action figures a lot, and she would never open one, because that would require to tear the wrapping. She also enjoys admiring all the figures, and the boxes only have one clear side, so putting a box back to front is out of question.
Help Lena to see if she could tell mom that cleaning cannon be finished, or if it’s possible and she has to arrange the boxes on the shelf anyway.
Input
The first line contains one integer n — the amount of boxes with action figures (1 ≤ n ≤ 100).
Each of next n lines contains a integer ki — amount of figures in i-th box (1 ≤ ki ≤ 100), followed by ki integers aij — sizes of action figures in order from left to right (1 ≤ aij ≤ 10^4). Integers in one line are separated with spaces.
Output
Print “YES” (without quotes), if boxes can be arranged in such a way that action figues would be in a non-decreasing order by their size. Otherwise, print “NO” (without quotes).
Samples
input	
3
2 1 2
3 7 7 7
1 5
output
YES

input
2
2 1 3
1 2
output
NO

Notes
In the first example, the first box goes first, then the third box, then the second box. That puts figures in a non-decreasing order by their size: 1, 2, 5, 7, 7, 7.
In the second example, there is no arrangement that puts figures in a non-decreasing order.
'''