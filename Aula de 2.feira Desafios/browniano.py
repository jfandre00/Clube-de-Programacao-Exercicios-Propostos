#Movimento Browniano
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
num_steps = 1000  # Número de passos
step_size = 1.0   # Tamanho do passo

# Inicializar as posições
x = np.zeros(num_steps)
y = np.zeros(num_steps)

# Gerar o movimento browniano
for i in range(1, num_steps):
    angle = np.random.uniform(0, 2 * np.pi)  # Escolhe um ângulo aleatório
    x[i] = x[i - 1] + step_size * np.cos(angle)  # Atualiza a posição X
    y[i] = y[i - 1] + step_size * np.sin(angle)  # Atualiza a posição Y

# Plotar o movimento browniano
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker='o', markersize=1, linestyle='-', color='blue')
plt.title('Simulação do Movimento Browniano')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.grid(True)
plt.show()
