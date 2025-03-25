#beecrowd 1890

# sistema de placas definido por dois numeros C e D, C consoantes seguidas por D digitos. Uma placa não pode ser vazia

# no alfabeto temos 44 consoantes e 10 digitos, mas utilizaremos somente 26 consoantes e 10 digitos

#o governo quer saber a quantidade de placas possiveis de serem feitas com C consoantes e D digitos


#entrada

t = int(input()) #numero de instancias

for i in range(t):
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        print(0)
    else: 
        print(26**c * 10**d) #26 consoantes e 10 digitos
    

