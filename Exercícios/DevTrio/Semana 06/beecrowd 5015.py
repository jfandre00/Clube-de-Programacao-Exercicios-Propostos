import math

N, X = map(int, input().split())


subscricoes = int(math.ceil(N/6))
#arredonda para cima o numero de subscricoes pois ate 6 pessoas podem usar o mesmo perfil

print(X*subscricoes)
