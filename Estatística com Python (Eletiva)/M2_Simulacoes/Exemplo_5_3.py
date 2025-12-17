
#
# Nome: Exemplo_5_3.py
# Função: Teste de hipótese para detecção em radares
# Data: 06/05/2020
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Sequência de 100 números

S1= np.ones(100)
S0= np.zeros(100)

Sinal= np.concatenate((S1,S0))
for iC in range(4):
    Sinal= np.concatenate((Sinal,S1,S0))
nS= len(Sinal)
N= np.arange(1, nS+1)

# Gerar ruído

mW= 0
sW= 0.5

W= np.random.normal(mW,sW,nS)

# Gerar sinal corrompido

SinalW= Sinal+W

# Gráficos

plt.plot(N,Sinal)
plt.xlabel('n')
plt.ylabel('Sinal')
plt.title('Sinal Original')
plt.grid()
plt.show()

plt.plot(N,SinalW)
plt.xlabel('n')
plt.ylabel('Sinal+W')
plt.title('Sinal Corrompido')
plt.grid()
plt.show()

plt.plot(N,SinalW,'r-',label='Sinal Corrompido')
plt.plot(N,Sinal,'b-',label='Sinal Original')
plt.xlabel('n')
plt.ylabel('Sinal')
plt.title('Sinal Original X Sinal Corrompido')
plt.grid()
plt.legend()

plt.show()

# TESTE DE HIPÓTESES 1

# Hipóteses
# H0: Tx 0 => Sinal = 0 + W => Sinal= N(mW,sW)
# H1: Tx 1 => Sinal = 1 + W => Sinal= N(1+mW,sW)

# PDFs

x = np.linspace(- 3*sW, 1 + 3*sW, 1000)

Pdf0= norm.pdf(x, 0, sW)
Pdf1= norm.pdf(x, 1, sW)

plt.plot(x,Pdf0,'b-',label='Pdf0')
plt.plot(x,Pdf1,'r-',label='Pdf1')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid()
plt.legend()
plt.show()

# Probabilidade de falso alarme X perda
# Valor crítico (xc)

Nc= np.linspace(0,0.8,100)
Xc= 0.6*np.ones(100)

plt.plot(x,Pdf0,'b-',label='Pdf0')
plt.plot(x,Pdf1,'r-',label='Pdf1')
plt.plot(Xc,Nc,'-k',label='valor crítico ???')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid()
plt.legend()
plt.show()

# pFA = 5% (0.05)       ... probabilidade da falso alarme
# pFA = P[x > xc | H0]  ... região de rejeição
# pFA = 1 - P[x <= xc | H0]
# pFA = 1 - Fx(xc | H0) ... Fx: função distribuição acumulada
# Fx(xc | Ho) = 1 - pFA
# xc = invFx(1 - pFA | H0)

pFA= 0.05
xc= norm.ppf(1-pFA,0,sW)
Xc= xc*np.ones(100)

plt.plot(x,Pdf0,'b-',label='Pdf0')
plt.plot(x,Pdf1,'r-',label='Pdf1')
plt.plot(Xc,Nc,'-k',label='valor crítico')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid()
plt.legend()
plt.show()


# Probabilidade de perda (missing) 
# pM = P[x <= xc | H1]
# pM = Fx(xc | H1)

pM= norm.cdf(xc, 1, sW) # ... problema ???

# Cálculo empírico de pFA e pM

# Regra de decisão
# se x <= xc => x = 0
# se x >  xc => x = 1

# Classificação do sinal

SinalR= 2*np.ones(nS) # sinal Reconstruído
cont_FA= 0
cont_M= 1

for iS in range (nS):
    
    xW= SinalW[iS]
    xS= Sinal[iS]
    
    if (xW >= xc):
        xR= 1
    else:
        xR= 0
        
    SinalR[iS]= xR
        
    if (xS != xR):
        if (xS == 0):
            cont_FA= cont_FA+1
        else:
            cont_M= cont_M+1

pFA_empirica= cont_FA/(nS/2)
pM_empirica= cont_M/(nS/2)

# Gráfico reconstrução

plt.plot(N,SinalR,'r-',label='Sinal Reconstruído')
plt.plot(N,Sinal,'b-',label='Sinal Original')
plt.xlabel('n')
plt.ylabel('Sinal')
plt.title('Sinal Original X Sinal Reconstruído')
plt.grid()
plt.legend()

plt.show() # ... ALUNOS => comentar o gráfico

# Solução => média

i1= 0
i2= 9
SinalWmed= np.zeros(nS)
for iB in range(100):
    
    mSW= np.mean(SinalW[i1:i2])
    SinalWmed[i1:i2]= mSW
    
    i1= i1+10
    i2= i2+10
    
plt.plot(N,SinalW,'r-',label='Sinal Corrompido')
plt.plot(N,Sinal,'b-',label='Sinal Original')
plt.xlabel('n')
plt.ylabel('Sinal')
plt.title('Sinal Original X Sinal Corrompido')
plt.grid()
plt.legend()

plt.show()

plt.plot(N,SinalWmed,'r-',label='Sinal Corrompido Médias')
plt.plot(N,Sinal,'b-',label='Sinal Original')
plt.xlabel('n')
plt.ylabel('Sinal')
plt.title('Sinal Original X Sinal Corrompido Médias')
plt.grid()
plt.legend()

plt.show()

# TESTE DE HIPÓTESES 2

# Hipóteses
# H0: Tx 0 => Sinal = 0 + W => Sinal= N(mW,sW/sqrt(10))
# H1: Tx 1 => Sinal = 1 + W => Sinal= N(1+mW,sW/sqrt(10)

# PDFs

nMed= 10
sWm= sW/np.sqrt(nMed)

#x = np.linspace(- 3*sWm, 1 + 3*sWm, 1000)

Pdf0med= norm.pdf(x, 0, sWm)
Pdf1med= norm.pdf(x, 1, sWm)

plt.plot(x,Pdf0,'b-',label='Pdf0')
plt.plot(x,Pdf0med,'g-',label='Pdf0 médias')
plt.plot(x,Pdf1,'r-',label='Pdf1')
plt.plot(x,Pdf1med,'m-',label='Pdf1 ´medias')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid()
plt.legend()
plt.show()

# Probabilidade de falso alarme X perda
# Valor crítico (xc)

Nc= np.linspace(0,2.5,100)
Xc= 0.2*np.ones(100)

plt.plot(x,Pdf0med,'b-',label='Pdf0 médias')
plt.plot(x,Pdf1med,'r-',label='Pdf1 médias')
plt.plot(Xc,Nc,'-k',label='valor crítico ???')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid()
plt.legend()
plt.show()

# pFA = 5% (0.05)       ... probabilidade da falso alarme
# pFA = P[x > xc | H0]  ... região de rejeição
# pFA = 1 - P[x <= xc | H0]
# pFA = 1 - Fx(xc | H0) ... Fx: função distribuição acumulada
# Fx(xc | Ho) = 1 - pFA
# xc = invFx(1 - pFA | H0)

pFA= 0.05
xcm= norm.ppf(1-pFA,0,sWm)
Xcm= xcm*np.ones(100)

plt.plot(x,Pdf0med,'b-',label='Pdf0 médias')
plt.plot(x,Pdf1med,'r-',label='Pdf1 médias')
plt.plot(Xcm,Nc,'-k',label='valor crítico')
plt.xlabel('x')
plt.ylabel('PDF')
plt.grid()
plt.legend()
plt.show()

# Probabilidade de perda (missing) 
# pM = P[x <= xc | H1]
# pM = Fx(xc | H1)

pMm= norm.cdf(xcm, 1, sWm) # ... problema ???

# Cálculo empírico de pFA e pM ====> ALUNOS





    







