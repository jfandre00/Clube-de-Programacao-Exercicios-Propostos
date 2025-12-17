N = int(input())

vogais = "aeiouAEIOU"

for _ in range(N):
    sobrenome = input().strip()

    consecutivas = 0       
    dificil = False        

    for letra in sobrenome:
        if letra not in vogais:
            consecutivas += 1
        else:
            consecutivas = 0

        # 3 ou mais consoantes consecutivas, nome dificil
        if consecutivas >= 3:
            dificil = True
            break

    if dificil:
        print(f"{sobrenome} nao eh facil")
    else:
        print(f"{sobrenome} eh facil")
