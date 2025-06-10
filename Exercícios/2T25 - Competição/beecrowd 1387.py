#conta os filhos com a mão esquerda e as filhas com a mão direita

while True:
    l, r = map(int, input().split())
    if l == 0 and r == 0:
        break
    filhos = 0

    print(l+r)