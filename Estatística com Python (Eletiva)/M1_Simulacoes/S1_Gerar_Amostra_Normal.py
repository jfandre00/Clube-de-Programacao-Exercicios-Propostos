
# Nome: S1_Gerar_Amostra_Normal.py
# Função: Gerar um aamostra com distribuição normal
# Data: 03/10/2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# parâmetros da normal
mu = 5      # média
sigma = 2   # desvio padrão
n = 10000   # número de amostras

# gerar amostras da normal
samples = np.random.normal(mu, sigma, n)

# eixo x para curva teórica
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = norm.pdf(x, mu, sigma)

# plotar histograma das amostras + curva teórica
plt.figure(figsize=(8,5))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='skyblue',
         label='Amostras (histograma)')
plt.plot(x, pdf, 'r-', lw=2, label='Curva Normal Teórica')
plt.title(f'Amostras de N({mu}, {sigma**2})')
plt.xlabel('x')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()


