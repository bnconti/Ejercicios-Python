# Exercise 3.26: Compute velocity and acceleration from 1D position data

"""
SAMPLE RUN:
Velocity: 150.0 - Acceleration: 0.00
Velocity: 150.0 - Acceleration: 0.00
"""


def kinematics(i, x, t):
    # x = position array
    # t = time array
    v_i = (x[i+1] - x[i-1]) / (t[i+1] - t[i-1])
    p1 = 2*((t[i+1] - t[i-1])**-1)
    p2 = ((x[i+1] - x[i])/(t[i+1] - t[i]))
    p3 = ((x[i] - x[i-1])/(t[i] - t[i-1]))
    a_i = p1 * (p2 - p3)
    return v_i, a_i


def test_kinematics():
    V = 150
    t = [0, 0.5, 1.5, 2.2]
    x = [time*V for time in t]
    for i in range(1, 3):
        v_i, a_i = kinematics(i, x, t)
        print("Velocity: {:.1f} - Acceleration: {:.2f}".format(v_i, abs(a_i)))

test_kinematics()

# If the velocity is constant, the acceleration will be equal to zero.
