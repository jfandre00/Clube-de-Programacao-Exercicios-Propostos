# a entrada contem varios casos de teste e termia com EOF
distancia_total = 0
numero_casos = 0


while True:
    try:
        nome = input()
        '''if nome == "":
            print(f"{(distancia_total/numero_casos if numero_casos > 0 else 0):.1f}")
            break'''
        distancia = int(input())
        distancia_total += distancia
        numero_casos += 1
        
    except EOFError:
        print(f"{(distancia_total/numero_casos if numero_casos > 0 else 0):.1f}")
        break


