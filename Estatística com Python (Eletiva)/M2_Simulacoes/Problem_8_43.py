#
# Nome: Problem_8_43.py
# Função: Problema 8.43
# Data: 06/05/2020
#

import numpy as np
from scipy.stats import chi2
from scipy.stats import t
from scipy.stats import norm

# ITEM (a)
# parâmetros da distribuição de X - Gaussian

n= 10
med_amostral= 57.3
var_amostral= 23.2

# probabilidades dos intervalos de confiança

p1= 0.90
p2= 0.95
p3= 0.99

# valores críticos da distribuição t'studant

t1= t.ppf(1-(1-p1)/2,n-1);
t2= t.ppf(1-(1-p2)/2,n-1);
t3= t.ppf(1-(1-p3)/2,n-1);

# intervalos de confiança

I90a= [med_amostral-t1*np.sqrt(var_amostral/n),med_amostral+t1*np.sqrt(var_amostral/n)]
I95a= [med_amostral-t2*np.sqrt(var_amostral/n),med_amostral+t2*np.sqrt(var_amostral/n)]
I99a= [med_amostral-t3*np.sqrt(var_amostral/n),med_amostral+t3*np.sqrt(var_amostral/n)]

# ITEM (b)

# ... para os alunos ...
# diferença de (a) para (b) ???

# I90 = [55.4377,59.1623]
# I95 = [55.0457,59.5543]
# I99 = [54.2187,60.3813]

# ITEM (c)

# parâmetros para o ítem c

n_10= 10
n_20= 20

# valores críticos da distribuição chiSquare

a1_10_1= chi2.ppf((1-p1)/2,n_10-1)
a2_10_1= chi2.ppf(1-(1-p1)/2,n_10-1)

a1_10_2= chi2.ppf((1-p2)/2,n_10-1)
a2_10_2= chi2.ppf(1-(1-p2)/2,n_10-1)

a1_10_3= chi2.ppf((1-p3)/2,n_10-1)
a2_10_3= chi2.ppf(1-(1-p3)/2,n_10-1)

a1_20_1= chi2.ppf((1-p1)/2,n_20-1)
a2_20_1= chi2.ppf(1-(1-p1)/2,n_20-1)

a1_20_2= chi2.ppf((1-p2)/2,n_20-1)
a2_20_2= chi2.ppf(1-(1-p2)/2,n_20-1)

a1_20_3= chi2.ppf((1-p3)/2,n_20-1)
a2_20_3= chi2.ppf(1-(1-p3)/2,n_20-1)

# intervalos de confiança

I90c_10= [(n_10-1)*var_amostral/a2_10_1,(n_10-1)*var_amostral/a1_10_1];
I95c_10= [(n_10-1)*var_amostral/a2_10_2,(n_10-1)*var_amostral/a1_10_2];
I99c_10= [(n_10-1)*var_amostral/a2_10_3,(n_10-1)*var_amostral/a1_10_3];

I90c_20= [(n_20-1)*var_amostral/a2_20_1,(n_20-1)*var_amostral/a1_20_1];
I95c_20= [(n_20-1)*var_amostral/a2_20_2,(n_20-1)*var_amostral/a1_20_2];
I99c_20= [(n_20-1)*var_amostral/a2_20_3,(n_20-1)*var_amostral/a1_20_3];


