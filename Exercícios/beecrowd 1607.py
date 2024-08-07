letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

n = 0

T = int(input())

while n < T:
    primeiro, segundo = map(str, input().split())
    total = 0

    for elemento in range(len(primeiro)):
        s = segundo[elemento]
        p = primeiro[elemento]
        quantidade = (letras.index(s)) - (letras.index(p))
        if quantidade < 0:
            quantidade = len(letras) + quantidade
        total += quantidade

    print(total)
    n +=1