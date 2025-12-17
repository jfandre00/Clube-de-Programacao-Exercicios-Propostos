
#
# Nome: Exemplo_5_6.py
# Função: Exemplo 5.6
# Data: 06/05/2020
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Limpa variáveis e console (equivalente a clear; clc;)
plt.close('all')

# Número de amostras
N = np.array([4, 16, 64, 256])
nN = len(N)

# Nível de significância
alfa = 0.1

# Faixa de médias alternativas
M1 = np.arange(-3, 3.01, 0.01)
nM1 = len(M1)

# Matriz do poder do teste
Pw = np.zeros((nM1, nN))

# Loop principal
for i, n in enumerate(N):

    # Valores críticos (teste bilateral)
    xc1 = norm.ppf(alfa / 2, loc=0, scale=np.sqrt(1 / n))
    xc2 = norm.ppf(1 - alfa / 2, loc=0, scale=np.sqrt(1 / n))

    # Cálculo do poder para cada média m1
    for j, m1 in enumerate(M1):
        beta = norm.cdf(xc2, loc=m1, scale=np.sqrt(1 / n)) - norm.cdf(xc1, loc=m1, scale=np.sqrt(1 / n))
        Pw[j, i] = 1 - beta

# ----- Gráfico -----
plt.figure(figsize=(8, 5))

plt.plot(M1, Pw[:, 0], label='n = 4')
plt.plot(M1, Pw[:, 1], label='n = 16')
plt.plot(M1, Pw[:, 2], label='n = 64')
plt.plot(M1, Pw[:, 3], label='n = 256')

plt.legend()
plt.xlabel('m₁')
plt.ylabel('1 - β(m₁)')
plt.title('Poder do teste')
plt.grid(True)
plt.show()

# Equivalente ao pause do MATLAB
input("Pressione Enter para fechar o gráfico...")
plt.close()


