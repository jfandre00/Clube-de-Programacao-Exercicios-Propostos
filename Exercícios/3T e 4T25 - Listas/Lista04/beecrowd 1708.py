X, Y = map(int, input().split())


diferenca = Y - X

voltas_para_alcancar = Y / diferenca


# arredonda para cima, se tiver resto, adiciona 1
print(int(voltas_para_alcancar) + (voltas_para_alcancar % 1 > 0)) 

# Quando faço voltas_para_alcancar % 1, estou verificando se há alguma parte fracionária em voltas_para_alcancar. Se for inteiro, o resultado será 0, então não há parte fracionária.
# Se voltas_para_alcancar for um número decimal (com parte fracionária) o resultado será maior que 0, 
# Então a expressão (voltas_para_alcancar % 1 > 0) retorna True (1) se houver
# parte fracionária e False (0) se não houver.
# Seria muito mais simples usar math.ceil() para arredondar para cima, mas quis fazer dessa forma para praticar operações matemáticas e lógicas.
