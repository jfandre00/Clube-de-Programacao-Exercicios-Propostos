# Nome: S3_Amostragem_Estratificada.py
# Função: Implementar uma amostragem estratificada
# Data: 09/10/2025

# Importação das bibliotecas 
import pandas as pd
from sklearn.model_selection import train_test_split

# Carregar base de dados 
iris = pd.read_csv('iris.csv')

print('População')
print(iris['class'].value_counts())

print('É uma base da dados balanceada ???')

# Gerar amostra estratificada

xTreino,xTeste,yTreino,yTeste = train_test_split(iris.iloc[:, 0:4],
                                                 iris.iloc[:, 4],
                                                 test_size= 0.1, 
                                                 stratify= iris.iloc[:,4])

print(' ')
print('Amostra')
print(yTeste.value_counts())

# Carregar nova base de dados
infert = pd.read_csv('infert.csv')

print(' ')
print('População 2')
print(infert['education'].value_counts())

print('É uma base da dados balanceada ???')

# Gerar amostra estratificada

x2Treino,x2Teste,y2Treino,y2Teste = train_test_split(infert.iloc[:, 2:9],
                                                     infert.iloc[:, 1],
                                                     test_size= 0.1,
                                                     stratify=infert.iloc[:,1])

print(' ')
print('Amostra 2')
print(y2Teste.value_counts())


