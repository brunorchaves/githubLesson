import matplotlib.pyplot as plt
import numpy as np
import random

# Criar uma figura com subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Primeiro subplot - Sinal de ruído
x_noise = np.linspace(0, 4 * np.pi, 100)
y_noise = np.random.normal(0, 0.5, len(x_noise))  # Ruído gaussiano

axs[0].plot(x_noise, y_noise, linestyle='-', color='b', label='Ruído Gaussiano')
axs[0].set_title("Gráfico de Ruído Gaussiano", fontsize=14)
axs[0].set_xlabel("x", fontsize=12)
axs[0].set_ylabel("Amplitude", fontsize=12)
axs[0].legend()
axs[0].grid(True, linestyle='--', alpha=0.7)

# Segundo subplot - Senoide com ruído
x_sin = np.linspace(0, 4 * np.pi, 100)  # Eixo x de 0 a 4π
y_sin = np.sin(x_sin) + np.random.normal(0, 0.1, len(x_sin))  # Seno de x com ruído gaussiano

axs[1].plot(x_sin, y_sin, linestyle='-', color='r', label='Senoide com Ruído')
axs[1].set_title("Gráfico de Senoide com Ruído", fontsize=14)
axs[1].set_xlabel("x", fontsize=12)
axs[1].set_ylabel("sen(x) + ruído", fontsize=12)
axs[1].legend()
axs[1].grid(True, linestyle='--', alpha=0.7)

# Terceiro subplot - FFT da senoide com ruído
freq = np.fft.fftfreq(len(x_sin), d=(x_sin[1] - x_sin[0]))
y_fft = np.fft.fft(y_sin)

axs[2].plot(freq[:len(freq)//2], np.abs(y_fft[:len(freq)//2]), linestyle='-', color='g', label='FFT da Senoide')
axs[2].set_title("Transformada de Fourier da Senoide", fontsize=14)
axs[2].set_xlabel("Frequência (Hz)", fontsize=12)
axs[2].set_ylabel("Magnitude", fontsize=12)
axs[2].legend()
axs[2].grid(True, linestyle='--', alpha=0.7)

# Ajustar layout
plt.tight_layout()

# Mostrar o gráfico
plt.show()
