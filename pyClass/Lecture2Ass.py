import numpy as np
import matplotlib.pyplot as plt

T0 = 500  # initial temperature
T_e = 300  # environment temperature
k = 0.1  # thermal conductivity
A = 1  # surface area
d = 0.1  # thickness
dt = 0.01  # time step
t_final = 100  # final time

time_points = []
temperature_points = []
heat_input_points = []

t = 0
T = T0
for i in range(int(t_final / dt)):
    dQdt = -((k * A) * (T - T_e) / d)
    T = T + dQdt * dt
    t += dt
    time_points.append(t)
    temperature_points.append(T)
    heat_input = -dQdt * dt * A * d
    heat_input_points.append(heat_input)
    print(f"{dQdt:.2f} {T:.2f} {t:.2f}s ")

time_points = np.array(time_points)
temperature_points = np.array(temperature_points)
heat_input_points = np.array(heat_input_points)

plt.plot(heat_input_points, temperature_points, color='r', label=r'$\frac{dx}{dt}$')
plt.xlabel('Heat Input (Q)')
plt.ylabel('Temperature (T)')
plt.title('Temperature vs. Heat Input')
plt.legend(fontsize=14)
plt.show()

slope, _ = np.polyfit(heat_input_points, temperature_points, 1)
volume = A * d
Cp = slope / volume
print(f"Specific heat capacity slope {slope:.2f}J / {volume}m^3: {Cp:.2f} J/kg.K)")
