try:
    while True:
        N = int(input())
        votos = [int(x) for x in input().split()]

        total_votos = 0
        for i in range (len(votos)): 
            total_votos += votos[i]

        if total_votos >= (2*N)/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
            
except EOFError:
    pass