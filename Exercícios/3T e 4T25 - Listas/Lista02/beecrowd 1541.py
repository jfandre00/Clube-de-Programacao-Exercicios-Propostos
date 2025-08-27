import math

while True:
    try: 
        a, b, c = map(int, input().split())

        area_casa = a * b
        tamanho_terreno = (area_casa * 100) / c

        lado_terreno = math.sqrt(tamanho_terreno)

        #print(f"{lado_terreno:.0f}") essa solução tinha dado erro pois pediu para truncar, então pensei em inteiro
        print(int(lado_terreno))
    except ValueError:
        # se o usuario entrar somente com 0, dá um break e encerra
        break