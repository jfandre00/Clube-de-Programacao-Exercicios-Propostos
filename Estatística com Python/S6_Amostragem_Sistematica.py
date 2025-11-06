# Nome: S2_Amostragem_Sistematica.py
# Função: Implementar uma amostragem sistematica
# Data: 09/10/2025

# Importação das bibliotecas
import numpy as np
import pandas as pd
from math import ceil

# Criação das variáveis para representar a população, a amostra e o valor de k
n_populacao = 150
n_amostra = 15
k = ceil(n_populacao / n_amostra)

# Definição do valor randômico para inicializar a amostra, iniciando em 1 até k 
r0= np.random.randint(low = 1, high = k , size = 1)
r= r0[0]

# Criar índice para a amostra

indices_amostra = []
for i in range(n_amostra):
    indices_amostra.append(r)
    r= r+k
    
# Gerar amostra
base = pd.read_csv('iris.csv')
base_amostra = base.loc[indices_amostra]

