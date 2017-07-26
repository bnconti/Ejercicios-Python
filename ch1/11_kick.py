# Exercise 1.11: Compute the air resistance on a football

"""
/usr/bin/python3.5 /home/bruno/PycharmProjects/EjerciciosPrimer/11_kick.py
Drag force of the football with velocity equal to 33.3 km/h = 5.1 kg m/s**2 
Drag force of the football with velocity equal to 8.3 km/h = 0.3 kg m/s**2 
Gravity force for both cases = 4.2 kg m/s**2

Process finished with exit code 0
"""

from math import pi

# Fd = drag force.
# Fg = gravity force.

# Fd = 1/2*Cd*Q*A*V**2
# Fg = mg, where g = 9.81 m/s**-2

rho = 1.2 # D = air density [kg m/s**-3]
a = 0.11 # a = ball radius = 11 cm.
A = pi*a**2 # A = Football cross-sectional area (normal to the velocity direction).
Cd = 0.2 # Cd = drag coefficient
m = 0.43 # m = Football mass [Kg].
g = 9.81 # g = Gravitational acceleration [m/s**-2]

speed_conversion = 1000.0/3600

Va = 120*speed_conversion
Vb = 30*speed_conversion

FdVa = 0.5*Cd*rho*A*Va**2
FdVb = 0.5*Cd*rho*A*Vb**2.

Fg = m*g

print("""\
Drag force of the football with velocity equal to {:.1f} km/h = {:.1f} kg m/s**2 
Drag force of the football with velocity equal to {:.1f} km/h = {:.1f} kg m/s**2 
Gravity force for both cases = {:.1f} kg m/s**2
""".format(Va, FdVa, Vb, FdVb, Fg))
