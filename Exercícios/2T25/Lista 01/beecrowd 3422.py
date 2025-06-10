n = int(input())

for i in range(n):
    tempoJogo, PrimeiroOuSegundo = map(str, input().split())
    tempoJogo = int(tempoJogo)
    if PrimeiroOuSegundo == "1T":
        if tempoJogo > 45:
            acrescimo = tempoJogo - 45
            print(f"45+{acrescimo}")
        else:
            print(f"{tempoJogo}") 
    else:
        tempoJogo = tempoJogo + 45
        if tempoJogo > 90:
            acrescimo = tempoJogo - 90
            print(f"90+{acrescimo}")
        else:
            print(f"{tempoJogo}")