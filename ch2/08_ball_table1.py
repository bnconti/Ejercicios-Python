# Exercise 2.8: Make a table of values from a formula

"""
SAMPLE RUN:
y(0.00) = 0.00
y(0.20) = 1.83
y(0.41) = 3.26
y(0.61) = 4.28
y(0.82) = 4.89
y(1.02) = 5.10
y(1.22) = 4.89
y(1.43) = 4.28
y(1.63) = 3.26
y(1.83) = 1.83
y(2.04) = 0.00
"""

v_0 = 10  # Initial velocity
g = 9.81  # Gravity

a = 0; b = 2*v_0/g; n = 10; h = (b-a)/n

intervals = [a+i*h for i in range(0, n+1)]

values = [v_0*t - 0.5*g*t**2 for t in intervals]

for i, v in zip(intervals, values):
    print("y({:.2f}) = {:.2f}".format(i, v))

# cont = 0
# values_alternative = []
# while cont <= n:
#     y = v_0*intervals[cont] - 0.5*g*intervals[cont]**2
#     values_alternative.append(y)
#     cont += 1
#
# print("-----------------")
#
# for i, v in zip(intervals, values_alternative):
#     print("y({:.2f}) = {:.2f}".format(i, v))
