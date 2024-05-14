import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

# Variables
l = 0.5          # Ancho de la apertura cuadrada
lam = 5e-7     # Longitud de onda
z = 1000          # Distancia de propagación
num_points = 10000

# Cálculo del número de Fresnel
Nf = (l/2)**2 / (lam*z)

# Cálculo del número de onda
k = (2*np.pi) / lam

# Definición del vector x
x = np.linspace(-l, l, num_points)

# Coeficientes para las funciones de Fresnel
coef1 = np.sqrt(2*Nf) * (1 - (2*x/l))
coef2 = np.sqrt(2*Nf) * (1 + (2*x/l))

# Cálculo de las funciones de Fresnel
S1, C1 = sc.fresnel(coef1)
S2, C2 = sc.fresnel(coef2)

# Cálculo de la onda compleja incidente
ix = ((1/np.sqrt(2)) * (C1+C2)) + ((1j/np.sqrt(2)) * (S1+S2))

# Cálculo de la onda difractada
u = (np.exp(1j*k*z)/1j) * ix

# Cálculo de la intensidad
intens = np.abs(u)**2

# Graficar intensidad vs (x/l)
# Graficar intensidad vs (x/l)
plt.plot(x/l, intens, color='blue')
plt.gca().set_facecolor('white')  
plt.hlines(1, -l/2, l/2, color='red', linestyle='--')
plt.vlines(-l/2, 0, 1, color='red', linestyle='--')
plt.vlines(l/2, 0, 1, color='red', linestyle='--')
plt.title('Intensidad vs (x/l)', color='black', fontsize=12)
plt.xlabel('x/l', color='black', fontsize=10)
plt.ylabel('Intensidad', color='black', fontsize=10)
plt.xticks(color='black', fontsize=8)
plt.yticks(color='black', fontsize=8)
plt.grid(False)
plt.text(0.8, 0.8, f'Nf={Nf:.2f}', color='black', transform=plt.gca().transAxes, fontsize=14)
plt.show()