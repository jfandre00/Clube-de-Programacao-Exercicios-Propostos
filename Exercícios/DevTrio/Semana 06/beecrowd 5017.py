N = int(input())
S = input().lower()
contador = 0

for letra in range(N):
    if S[letra] in ("a", "e", "i", "o", "u"):
        contador = 0
    else:
        contador += 1
        if contador == 4:
            print("NO")
            break

if contador < 4:
    print("YES")