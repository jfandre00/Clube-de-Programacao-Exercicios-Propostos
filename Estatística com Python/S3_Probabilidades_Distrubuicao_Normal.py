
# Nome: S3_Probabilidades_Distrubuicao_Normal.py
# Função: Cálculos das probabilidades em uma distribuição normal
# Data: 03/10/2025

from scipy.stats import norm

# Parâmetros da normal
mu, sigma = 0, 1   # Normal padrão
a, b = -1, 1       # Intervalo

# P[x <= a] = F(a) 
p1= norm.cdf(a, mu, sigma)
print("P(X <= a) = p1 =", p1)

# P[x >= b] = 1 - F(b) 
p2= 1-norm.cdf(b, mu, sigma)
print("P(X >= b) = p2 =", p2)

# P[a <= x <= b] = F(b) - F(a)
p3 = norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma)
print("P(a <= X <= b) = p3 =", p3)




