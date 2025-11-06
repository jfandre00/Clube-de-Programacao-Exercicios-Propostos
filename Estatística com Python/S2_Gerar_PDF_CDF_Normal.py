
# Nome: S2_Gerar_PDF_CDF_Normal.py
# Função: Cálculos da probabilidade em uma distribuição normal
# Data: 03/10/2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 0, 1
x = np.linspace(-4, 4, 1000)

pdf = norm.pdf(x, mu, sigma)  # Função densidade
cdf = norm.cdf(x, mu, sigma)  # Função acumulada

plt.figure(figsize=(10,4))

# PDF
plt.subplot(1,2,1)
plt.plot(x, pdf, 'b', label='PDF')
plt.fill_between(x, pdf, alpha=0.3)
plt.title("PDF - Densidade")
plt.xlabel("x"); plt.ylabel("f(x)")
plt.legend()

# CDF
plt.subplot(1,2,2)
plt.plot(x, cdf, 'r', label='CDF')
plt.title("CDF - Acumulada")
plt.xlabel("x"); plt.ylabel("F(x)")
plt.legend()

plt.tight_layout()
plt.show()



