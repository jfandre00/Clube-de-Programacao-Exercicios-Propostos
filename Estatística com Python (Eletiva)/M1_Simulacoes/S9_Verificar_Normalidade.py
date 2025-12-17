# Nome: S4_Verificar_Normalidade.py
# Função: Verificar se uma amostra de dados apresenta distribuição normal
# Data: 10/10/2025

# Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Gerar amostra normal
n_amostra= 10000
mu= 0
sigma= 1
AmostraN= np.random.normal(mu, sigma, n_amostra)

# Gerar amostra uniforme
nMin= -2
nMax= 2
AmostraU= np.random.uniform(nMin,nMax,n_amostra)

# Gráficos das amostras

plt.subplot(211)
plt.plot(AmostraN)
plt.ylabel('Amostra Normal')
plt.grid()

plt.subplot(212)
plt.plot(AmostraU)
plt.ylabel('Amostra Uniforme')
plt.xlabel('n')

plt.grid()
plt.show()

# ALUNOS
# Observações sobre os gráficos

# Verificação

# Estatísticas das amostras
mN= np.mean(AmostraN)
sN= np.std(AmostraN)

mU= np.mean(AmostraU)
sU= np.std(AmostraU)

# Gerar pdf teórica (Normal) para as amostras
x = np.linspace(-3, 3, n_amostra)
pdfN = norm.pdf(x, mN, sN)  # Função densidade
pdfU = norm.pdf(x, mU, sU)  # Função densidade

# Histograma da AmostraN (pdf real) X pdf teórica da AmostraN
plt.figure(figsize=(8,5))
plt.hist(AmostraN, bins=50, density=True, alpha=0.6, color='skyblue',
         label='Amostras (histograma)')
plt.plot(x, pdfN, 'r-', lw=2, label='Curva Normal Teórica')
plt.title('AmostraN')
plt.xlabel('x')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# Histograma da AmostraU (pdf real) X pdf teórica da AmostraU
plt.figure(figsize=(8,5))
plt.hist(AmostraU, bins=50, density=True, alpha=0.6, color='skyblue',
         label='Amostras (histograma)')
plt.plot(x, pdfU, 'r-', lw=2, label='Curva Normal Teórica')
plt.title('AmostraU')
plt.xlabel('x')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True)
plt.show()

# ALUNOS
# Análise dos gráficos
# Conclusão





