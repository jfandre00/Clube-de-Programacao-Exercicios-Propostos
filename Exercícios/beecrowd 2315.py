from datetime import date

# Leitura das datas de entrada e separação em dia e mês
d0 = input().split()  # Input da primeira data
d1 = input().split()  # Input da segunda data

# Criação dos objetos date para cada data no ano de 2007
d0 = date(2007, int(d0[1]), int(d0[0]))  # Formato: date(ano, mês, dia)
d1 = date(2007, int(d1[1]), int(d1[0]))

# Cálculo da diferença entre as datas em dias
dif = d1 - d0

# Impressão do número de dias de diferença
print(dif.days)
