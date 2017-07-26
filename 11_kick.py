"""Exercise 1.11: Compute the air resistance on a football
The drag force, due to air resistance, on an object can be expressed as

Fd = 1/2*Cd*Q*A*V**2

where Q is the density of the air, V is the velocity of the object, A is the cross-
sectional area (normal to the velocity direction), and Cd is the drag coefficient,
which depends heavily on the shape of the object and the roughness of the surface.

The gravity force on an object with mass m is Fg = mg, where g = 9.81 m/s**-2.

We can use the formulas for Fd and Fg to study the importance of air resistance
versus gravity when kicking a football. The density of air is D = 1.2 kg m/s**-3. We
have A = pi*a**2 for any ball with radius a. For a football, a = 11 cm and the mass
is 0.43 kg. The drag coefficient Cd varies with the velocity and can be taken as 0.4.

Make a program that computes the drag force and the gravity force on a football.
Write out the forces with one decimal in units of Newton (N = kg m/s**2 ). Also
print the ratio of the drag force and the gravity force. Define Cd, D, A, V , m, g,
Fd, and Fg as variables, and put a comment with the corresponding unit. Use the
program to calculate the forces on the ball for a hard kick, V = 120 km/h and for
a soft kick, V = 30 km/h (it is easy to mix inconsistent units, so make sure you
compute with V expressed in m/s).
"""

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