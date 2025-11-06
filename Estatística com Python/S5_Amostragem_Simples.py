# Nome: S1_Amostragem_Simples.py
# Função: Implementar uma amostragem simples
# Data: 08/10/2025

# Importação das bibliotecas
import pandas as pd
import numpy as np

# Carregamento da base de dados 
base = pd.read_csv("C:\\Users\\jfand\\OneDrive\\Documents\\MeusProjetos\\Clube-de-Programacao-5f-Exercicios-Propostos\\Testes André\\iris.csv")

# Verificar tamanho base de dados
Dim= base.shape
nL= Dim[0]
nC= Dim[1]

# Mudança da semente aleatória randômica para manter os resultados em várias execuções\n",
np.random.seed(2345)

# 150 amostras, de 0 a 1, com reposição, probabilidades equivalentes
indica_amostra = np.random.choice(a = [0, 1], size = nL, replace = True,
                                  p = [0.9, 0.1])

# Base amostra
base_amostra = base.loc[indica_amostra == 1]
