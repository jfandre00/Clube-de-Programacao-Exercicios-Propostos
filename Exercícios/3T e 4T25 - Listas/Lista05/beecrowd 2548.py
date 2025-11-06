while True:
    try:
        N, M = map(int, input().split())
        valores = list(map(int, input().split()))
        
        if M == 0:
            print(0)
        else:
            print(sum(valores[-M:]))
    except EOFError:
        break