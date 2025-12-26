C, n = map(int, input().split())

passageiros = 0
possible = True

for i in range(n):
    sai, entra, espera = map(int, input().split())
    
    # Pessoas saem
    passageiros -= sai
    if passageiros < 0:
        possible = False
        break
    
    # Pessoas entram
    passageiros += entra
    if passageiros > C:
        possible = False
        break
    
    # Se alguém esperou, o trem deve estar cheio
    if espera > 0 and passageiros < C:
        possible = False
        break
    
    # Na última estação ninguém pode esperar
    if i == n - 1 and espera > 0:
        possible = False
        break

# O trem deve terminar vazio
if passageiros != 0:
    possible = False

if possible:
    print("possible")
else:
    print("impossible")
