entrada = list(map(int, input().split()))
maximizar = input()
calculo = 0

if maximizar == "A":
    resultado = entrada[0]
    calculo = ((entrada[1]/2) * 3) + ((entrada[2]/2) * 5)
    calculo = int(calculo)
    resultado += calculo

    print(resultado)

    
if maximizar == "B":
    resultado = entrada[1]
    calculo = ((entrada[0]/3) *2) + ((((entrada[2]/2) * 5)/3) * 2)
    calculo = int(calculo)
    resultado += calculo

    print(resultado)


if maximizar == "C":
    resultado = entrada[2]
    calculo = ((entrada[0]/5) * 2) + ((((entrada[1]/2) * 3)/5) * 2)
    calculo = int(calculo)
    resultado += calculo

    print(resultado)