# Lê quatro valores reais na mesma linha:
# A = preço do álcool
# G = preço da gasolina
# Ra = rendimento (km/l) com álcool
# Rg = rendimento (km/l) com gasolina
A, G, Ra, Rg = map(float, input().split())

# Calcula o custo por km de cada combustível
custo_alcool = A / Ra
custo_gasolina = G / Rg

# Se álcool for mais barato, imprime 'A'
# Caso contrário (igual ou mais caro), 'G'
if custo_alcool < custo_gasolina:
    print("A")
else:
    print("G")
