
# Nome: S4_Teorema_Limite_Central.py
# Função: Simulação do TLC
# Data: 03/10/2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da população
pop_size = 100000
a, b = 0, 10  # Distribuição uniforme entre 0 e 10
population = np.random.uniform(a, b, pop_size)

# Parâmetros da amostragem
n_samples = 10000  # Quantas amostras vamos tirar
sample_size = 30    # Tamanho de cada amostra

# Calcular médias de cada amostra
sample_means = []
for _ in range(n_samples):
    sample = np.random.choice(population, sample_size, replace=True)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# Estatísticas teóricas da média amostral
mu = (a + b) / 2
sigma = (b - a) / np.sqrt(12)  # Desvio padrão da população uniforme
std_error = sigma / np.sqrt(sample_size)

# Plotando a distribuição da população
plt.hist(population, bins=50, density=True, alpha=0.6, color='skyblue',
         label="Médias amostrais")
plt.title(f"Distribuição população (Uniforme entre {a} e {b})")
plt.xlabel("população")
plt.ylabel("Densidade")
plt.show()

# Plotando a distribuição das médias amostrais
x = np.linspace(min(sample_means), max(sample_means), 1000)
plt.hist(sample_means, bins=50, density=True, alpha=0.6, color='skyblue',
         label="Médias amostrais")

# Sobrepondo a curva normal teórica
plt.plot(x, norm.pdf(x, mu, std_error), 'r', lw=2,
         label="Curva Normal Teórica")
plt.title("Teorema do Limite Central")
plt.xlabel("Média da amostra")
plt.ylabel("Densidade")
plt.legend()
plt.show()





