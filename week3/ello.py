import numpy as np
import matplotlib.pyplot as plt

# Parameter
phi = np.linspace(0.01, 0.4, 100)  # porositas
rho_w = 0.3  # fluida (Ohm-m)
rho_c = 5.0  # clay (Ohm-m)

# Konversi ke konduktivitas
sigma_w = 1 / rho_w
sigma_c = 1 / rho_c

# Archie
a = 1
m = 2
rho_archie = a * rho_w * phi**(-m)

# Geometric Mean
rho_geo = rho_w**phi * rho_c**(1 - phi)

# Hashin-Shtrikman Bounds (dalam konduktivitas)
sigma_HS_lower = sigma_c + phi / ((1/(sigma_w - sigma_c)) + (1 - phi)/(3*sigma_c))
sigma_HS_upper = sigma_w + (1 - phi) / ((1/(sigma_c - sigma_w)) + phi/(3*sigma_w))

# Balik ke resistivitas
rho_HS_lower = 1 / sigma_HS_lower
rho_HS_upper = 1 / sigma_HS_upper

# Plot
plt.figure()

plt.plot(phi, rho_archie, label='Archie Law')
plt.plot(phi, rho_geo, label='Geometric Mean')
plt.plot(phi, rho_HS_lower, '--', label='HS Lower Bound')
plt.plot(phi, rho_HS_upper, '--', label='HS Upper Bound')

plt.axhline(y=10, linestyle=':', label='Batas 10 Ohm-m')

plt.xlabel('Porositas')
plt.ylabel('Resistivitas (Ohm-m)')
plt.title('Perbandingan Model Resistivitas Batuan')
plt.legend()
plt.grid()

plt.show()