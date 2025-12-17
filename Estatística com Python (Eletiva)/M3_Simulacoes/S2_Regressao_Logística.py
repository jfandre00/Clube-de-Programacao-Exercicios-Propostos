
#
# Nome: S2_Regressao_Logística.py
# Função: Aplicação do modelo de regressão logística 
# Base de Dados: Breast Cancer Wisconsin (diagnostics)
#                UCI - Machine Learning Repository
# Aplicação: Classificação Binária
# Data: 18/05/2022

import numpy as np
import matplotlib.pyplot as plt

# Leitura da Base de Dados

import pandas as pd

X= pd.read_csv('Dados_Entrada_Breast_Cancer.csv')   # Previsores

Y= pd.read_csv('Dados_Saida_Breast_Cancer.csv')     # Classe
                                                    # Y= 0 => cancer benigno
                                                    # Y= 1 => cancer maligno
                                                    
# Separação da base de dados em teste e treinamento

from sklearn.model_selection import train_test_split

X_treino,X_teste,Y_treino,Y_teste= train_test_split(X,Y,test_size= 0.25)

# Modelo

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_treino, Y_treino)

# Classificação / Previsão

from sklearn.metrics import accuracy_score

Y_prev = model.predict(X_teste)
Y_prev_prob = model.predict_proba(X_teste)

acerto= accuracy_score(Y_teste,Y_prev)


                                                   

