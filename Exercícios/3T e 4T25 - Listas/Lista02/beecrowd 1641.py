'''A pizza cabe se a diagonal do retângulo for menor ou igual ao diâmetro da mesa.
Isso pq a mesa é um círculo e o retângulo vai caber dentro dele se a diagonal do retângulo for no máximo igual ao diâmetro do círculo.'''

import math

contador = 0

while True:
    RWL = input().strip() #forma diferente de ler a entrada, sem precisar do try / except ValueError
    if RWL == "0": #se o usuário digitar 0, o loop é interrompido
        break

    R, W, L = map(int, RWL.split()) #desmembrando os valores de R, W e L
    contador += 1

    diagonal_pizza = math.sqrt(W**2 + L**2) #calculando a diagonal da pizza, hipotenusa do triângulo retângulo formado por W e L (meia pizza)
    diametro_mesa = 2 * R

    if diagonal_pizza <= diametro_mesa: #se a diagonal da pizza for menor ou igual ao diâmetro da mesa - Dessa forma não preciso comparar as áreas, como tinha feito antes e não estava dando certo (pois as área mede o espaço total que ocupa, não o formato). 
        print(f"Pizza {contador} fits on the table.")
    else:
        print(f"Pizza {contador} does not fit on the table.")
