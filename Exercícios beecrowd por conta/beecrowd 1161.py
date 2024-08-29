#Soma de fatoriais - Beecrowd 1161
#varios casos de teste


while True:
    try:
        primeiro, segundo = map(int, input().split())

        def fatorial(n):
            if n == 0:
                return 1
            return n * fatorial(n-1)

        print(fatorial(primeiro) + fatorial(segundo))
    except EOFError:
        break
    