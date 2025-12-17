
#
# Nome: Exemplo_5_5.py
# Função: Exemplo 5.5
# Data: 06/05/2020
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Vetor de tamanhos de amostra
N = np.array([4, 9, 25, 100])

nN = len(N)

# Valor crítico (não usado diretamente aqui, mas calculado)
XC = np.zeros(nN)

# Intervalo de médias alternativas
M1 = np.arange(150, 160.1, 0.1)  # equivalente a 150:0.1:160
nM1 = len(M1)

# Matriz do poder do teste
Pw = np.zeros((nM1, nN))

# Loop principal
for i, n in enumerate(N):
    xc = norm.ppf(0.99, loc=150, scale=np.sqrt(16/n))
    XC[i] = xc  # guarda o valor crítico
    
    for j, m1 in enumerate(M1):
        Pw[j, i] = 1 - norm.cdf(xc, loc=m1, scale=np.sqrt(16/n))

# Exemplo: imprimir parte dos resultados
print("Valores críticos:", XC)

# ----- Gráfico -----
plt.figure(figsize=(8, 5))

plt.plot(M1, Pw[:, 0], label='n = 4')
plt.plot(M1, Pw[:, 1], label='n = 9')
plt.plot(M1, Pw[:, 2], label='n = 25')
plt.plot(M1, Pw[:, 3], label='n = 100')

plt.legend()
plt.xlabel('m₁')
plt.ylabel('1 - β(m₁)')
plt.title('Poder do teste X')
plt.grid(True)
plt.show()

# Equivalente ao 'pause' do MATLAB:
input("Pressione Enter para fechar o gráfico...")

plt.close()
