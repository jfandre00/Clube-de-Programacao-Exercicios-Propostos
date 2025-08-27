numero_postos_agua, distancia_intermediaria_maxima = map(int, input().split())
lista_de_postos = list(map(int, input().split()))

# Adiciona a chegada como último ponto
lista_de_postos.append(42195)

consegue = True
for i in range(len(lista_de_postos) - 1):
    if lista_de_postos[i+1] - lista_de_postos[i] > distancia_intermediaria_maxima:
        consegue = False
        break

print("S" if consegue else "N")
