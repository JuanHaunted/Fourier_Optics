"""
Optica de Fourier
Transformada de Fourier a un circulo blanco en un fondo negro
Despues se grafica un patron de Airy

Realizado por: Jacobo Chica
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import airy

img = np.zeros((1000, 1000), dtype='uint8')

for i in range (500):
  for j in range(500):
    if np.sqrt(i**2 + j**2)<10:
      img[i+(img.shape[1] // 2), j + (img.shape[0] // 2)] = 1
      img[i+(img.shape[1] // 2), (img.shape[0] // 2)-j] = 1
      img[(img.shape[1] // 2)-i, j + (img.shape[0] // 2)] = 1
      img[(img.shape[1] // 2)-i, (img.shape[0] // 2)-j] = 1

img_fft = np.fft.ifftshift (np.fft.fft2 (np.fft.fftshift(img)))
img_fft = img_fft.real

plt.subplot(1, 2, 2), plt.imshow(img)
plt.imshow(img, cmap='gray')
plt.title('Circulo original')

plt.subplot(1, 2, 1), plt.imshow(img_fft)
plt.imshow(img_fft, cmap='gray')
plt.title('Circulo FFT')

plt.show()



# Defición de parámetros
radio = 50.0   # del disco
lamnda = 0.25  # Longitud de onda
dist_centro = 15.0  # Distancia desde el centro
dim = 1000  # Tamaño de la imagen

# Generar malla de coordenadas
x = np.linspace(-dim/2, dim/2, dim)
y = np.linspace(-dim/2, dim/2, dim)
x, y = np.meshgrid(x, y)

# Calcular la función de Airy
airy_f = airy(np.sqrt((x/radio)**2 + (y/radio)**2) / (lamnda * dist_centro))[0]

# Grafico
plt.imshow(np.abs(airy_f)**2, cmap='gray', extent=[-dim/2, dim/2, -dim/2, dim/2])
plt.title('Disco de Airy')
plt.show()




