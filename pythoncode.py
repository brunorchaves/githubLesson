import matplotlib.pyplot as plt
import random

# Gerar números aleatórios
x = list(range(1, 21))  # Eixo x (1 a 20)
y = [random.randint(1, 100) for _ in x]  # Eixo y com números aleatórios entre 1 e 100

# Criar o gráfico
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Números Aleatórios')

# Adicionar títulos e rótulos
plt.title("Gráfico de Números Aleatórios", fontsize=14)
plt.xlabel("Índice", fontsize=12)
plt.ylabel("Valor Aleatório", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar o gráfico
plt.show()