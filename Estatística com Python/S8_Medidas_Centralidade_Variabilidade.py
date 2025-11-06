# Nome: S4_Medidas_Centralidade_Variabilidade.py
# Função: Cálculo das Medidas de centralidade e variabilidade
# Data: 10/10/2025

# Importação das bibliotecas: scipy para gerar estatísticas mais detalhadas
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# parâmetros das amostras com distribuição normal
mu1 = 0      # média
mu2 = 2
sigma1 = 1   # desvio padrão
sigma2 = 2   # desvio padrão
n = 10000    # número de amostras

# gerar amostras da normal
Samples1 = np.random.normal(mu1, sigma1, n)
Samples2 = np.random.normal(mu2, sigma2, n)

N= np.arange(1, n+1)

# mostrar amostra

plt.subplot(211)
plt.ylim(-10,10)
plt.plot(N,Samples1)
plt.ylabel('Amostra 1')
plt.grid()

plt.subplot(212)
plt.ylim(-10,10)
plt.plot(N,Samples2)
plt.ylabel('Amostra 2')
plt.xlabel('n')

plt.grid()
plt.show()

# ALUNOS
# Comparar os gráficos em centralidade e variabilidade

# Médias
m1= np.mean(Samples1)
m2= np.mean(Samples2)

# Desvio padrão
s1= np.std(Samples1)
s2= np.std(Samples2)

# ALUNOS
# Avaliar as medidas de centralidade e variabilidade com os gráficos

# Escrever um script para calcular a média e o desvio padrão de ambas as amostras


### Lição que o professor passou:
# ===========================================
# Cálculo da média e do desvio padrão em Python puro
# ===========================================

# Função para calcular a média
def media(lista):
    return sum(lista) / len(lista)

# Função para calcular o desvio padrão
def desvio_padrao(lista):
    m = media(lista)
    variancia = sum((x - m) ** 2 for x in lista) / len(lista)  # cálculo da variância -> média dos quadrados das diferenças em relação à média 
    '''
    variancia = sum((x - m) ** 2 for x in lista) / (len(lista) - 1)  # cálculo da variância amostral (dividindo por n-1)
    '''

    return variancia ** 0.5 # retornando o desvio padrão (raiz quadrada da variância)

# Cálculos
m1_puro = media(Samples1)
m2_puro = media(Samples2)

s1_puro = desvio_padrao(Samples1)
s2_puro = desvio_padrao(Samples2)

# Exibir resultados
print("===== Medidas de Centralidade e Variabilidade (feito em Python puro) =====")
print(f"Amostra 1 -> Média: {m1_puro:.4f} | Desvio Padrão: {s1_puro:.4f}")
print(f"Amostra 2 -> Média: {m2_puro:.4f} | Desvio Padrão: {s2_puro:.4f}")






