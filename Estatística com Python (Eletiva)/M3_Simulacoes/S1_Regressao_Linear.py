
#

#
# Nome: S1_Regressao_Linear.py
# Função: Aplicação do modelo de regressão linear em dois conjuntos de dados
# Data: 11/11/2025
#

# Importação das bibliotecas

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do ruído

mW= 0; 
sW= 1;
n= 100;

W= np.random.normal(mW,sW, n)

# Variável dependente

X= np.arange(1, 11,0.1) # start, stop, step

# Variáveis independentes

a0= 0 
a1= 1

Y1= a0+a1*X+1*W

Y2= np.exp(1*X)+3000*W

# Gráficos de dispersão

plt.plot(X,Y1,'.')
plt.xlabel('X')
plt.ylabel('Y1')
plt.title('Gráfico de dispersão')
plt.grid()
plt.show()

plt.plot(X,Y2,'.')
plt.xlabel('X')
plt.ylabel('Y2')
plt.title('Gráfico de dispersão')
plt.grid()
plt.show()

# Correlação de coeficiente de determinação

corr_matrix = np.corrcoef(X,Y1)
r_1 = corr_matrix[0, 1]
R2_1= r_1**2

corr_matrix = np.corrcoef(X,Y2)
r_2 = corr_matrix[0, 1]
R2_2= r_2**2

# Parâmetros b0 e b1 estimados do modelo de regressão

mX= np.mean(X)   # médias
mY1= np.mean(Y1) 
mY2= np.mean(Y2) 

b1_1 = np.sum((X - mX) * (Y1 - mY1)) / np.sum((X-mX)**2) # b1 estimado
b1_2 = np.sum((X - mX) * (Y2 - mY2)) / np.sum((X-mX)**2)

b0_1 = mY1 - b1_1 * mX # b0 estimado
b0_2 = mY2 - b1_2 * mX

# Estimativas

Y1_est= b0_1+b1_1*X

Y2_est= b0_2+b1_2*X 

# Resíduos

Res_1= Y1-Y1_est

Res_2= Y2-Y2_est

# Gráficos modelo 1

plt.plot(X,Y1,'.',label='Y1')
plt.plot(X,Y1_est,label='Y1_est')
plt.xlabel('X')
plt.ylabel('Y1 e Y1_est')
plt.title('Modelo 1')
plt.legend()
plt.grid()
plt.show()

plt.plot(X,Res_1,'.')
plt.xlabel('X')
plt.ylabel('Res_1')
plt.title('Resíduos Modelo 1')
plt.grid()
plt.show()

# Gráficos modelo 2

plt.plot(X,Y2,'.',label='Y2')
plt.plot(X,Y2_est,label='Y2_est')
plt.xlabel('X')
plt.ylabel('Y2 e Y2_est')
plt.title('Modelo 2')
plt.legend()
plt.grid()
plt.show()

plt.plot(X,Res_2,'.')
plt.xlabel('X')
plt.ylabel('Res_2')
plt.title('Resíduos Modelo 2')
plt.grid()
plt.show()

# Previsão
# X = [0,11]
# X > 11
# Y1= ?
# Y2= ?

w= 1*np.random.normal(mW,sW, 1)
x= 12 # 12, 20, 100

y1= a0+a1*x+w      # valor real
y2= np.exp(1*x)+3000*w

y1_est= b0_1+b1_1*x   # valor estimado
y2_est= b0_2+b1_2*x

erro_y1= y1-y1_est   # erro da previsão
erro_y2= y2-y2_est

erro_y1_per= (erro_y1/y1)*100 # erro da previsão %
erro_y2_per= (erro_y2/y2)*100
