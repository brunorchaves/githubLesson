import matplotlib.pyplot as plt
import numpy as np
import random

# Gerar números aleatórios
x = list(range(1, 21))  # Eixo x (1 a 20)
y = [random.randint(1, 100) for _ in x]  # Eixo y com números aleatórios entre 1 e 100

# Criar uma figura com subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Primeiro subplot - Gráfico de números aleatórios
axs[0].plot(x, y, marker='o', linestyle='-', color='b', label='Números Aleatórios')
axs[0].set_title("Gráfico de Números Aleatórios", fontsize=14)
axs[0].set_xlabel("Índice", fontsize=12)
axs[0].set_ylabel("Valor Aleatório", fontsize=12)
axs[0].legend()
axs[0].grid(True, linestyle='--', alpha=0.7)

# Segundo subplot - Senoide
x_sin = np.linspace(0, 4 * np.pi, 100)  # Eixo x de 0 a 4π
y_sin = np.sin(x_sin)  # Seno de x

axs[1].plot(x_sin, y_sin, linestyle='-', color='r', label='Senoide')
axs[1].set_title("Gráfico de Senoide", fontsize=14)
axs[1].set_xlabel("x", fontsize=12)
axs[1].set_ylabel("sen(x)", fontsize=12)
axs[1].legend()
axs[1].grid(True, linestyle='--', alpha=0.7)

# Ajustar layout
plt.tight_layout()

# Mostrar o gráfico
plt.show()
