def mount_marathon(n, cartas):
    pilhaDeCartas = cartas[:] 

    while True:
        movido = False  
        i = 0
        
        while i < len(pilhaDeCartas) - 1:
            if pilhaDeCartas[i] >= pilhaDeCartas[i + 1]:
                pilhaDeCartas[i + 1] = pilhaDeCartas[i]
                pilhaDeCartas.pop(i)
                movido = True  
            else:
                i += 1  
        
        if not movido:
            break  

    return len(pilhaDeCartas)

n = int(input()) 
cartas = list(map(int, input().split()))  

print(mount_marathon(n, cartas))