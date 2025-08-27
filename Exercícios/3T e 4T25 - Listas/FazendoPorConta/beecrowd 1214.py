acc = 0
soma_notas = 0
    
casos = int(input())
for _ in range(casos):

    media_final = list(map(int, input().split()))

    numero_casos = media_final[0]
    media_final.pop(0)

    soma_notas = sum(media_final)

    media_turma = soma_notas / numero_casos

    acc = sum(1 for nota in media_final if nota > media_turma)

    print(f"{acc/numero_casos * 100:.3f}%")

    media_final.clear()
    acc = 0
    soma_notas = 0
