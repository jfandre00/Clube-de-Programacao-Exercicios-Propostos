# Ler o número de animais e abaixo uma lista com os tipos de animais (que são números)
N = int(input())
animals = list(map(int, input().split()))

# Verificar se o número total de animais é par
if N % 2 != 0:
    print("NO")
else:
    '''Cada tipo de animal é representado por um número na lista. O objetivo é contar quantas vezes cada número aparece na lista e verificar se todas essas contagens são pares. Se todas as contagens forem pares, então é possível dividir os animais de forma que Alice e Bob tenham exatamente o mesmo multiconjunto de animais.'''   
    animal_count = {}
    for animal in animals:
        if animal in animal_count:
            animal_count[animal] += 1
        else:
            animal_count[animal] = 1
    
    # Verificar se todas as frequências são pares
    possible = True
    for count in animal_count.values():
        if count % 2 != 0:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")