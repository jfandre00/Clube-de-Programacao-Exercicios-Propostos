#
# Nome: Problem_8_46.py
# Função: Problema 8.46
# Data: 06/05/2020
#

import numpy as np
from scipy.stats import chi2
from scipy.stats import t
from scipy.stats import norm

# ITEM (a)

# parâmetros da distribuição

med= 0
var= 1
desvpad= np.sqrt(var)
std= np.sqrt(var)
n= 10

p= 0.9;

# valor crítico da distribuição normal

z = norm.ppf(1-(1-p)/2, loc=med, scale=std)

# intervalos de confiança

I90= [med-z*np.sqrt(var/n),med+z*np.sqrt(var/n)]

# ITEM (b)

N_amostras= 500  # número de amostras
n_amostra= 10    # tamanho da amostra
cont= 0

for i_amostras in range(N_amostras):
    
    Amostra= np.random.normal(med,desvpad,n_amostra) # geração da amostra
    mAmostra= np.mean(Amostra)                       # média da amostra
    
    if(I90[0] <= mAmostra <= I90[1]):                # verifica se está debtro
                                                     # do intervalo
        cont= cont+1
        
p90= cont/N_amostras  # estima a probabilidade
    
# ITEM (c)
# ... para os alunos ...    


