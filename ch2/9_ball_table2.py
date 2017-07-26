# Exercise 2.9: Store values from a formula in lists

v_0 = 10  # Initial velocity
g = 9.81  # Gravity

a = 0; b = 2*v_0/g; n = 10; h = (b-a)/n

intervals = [a+i*h for i in range(0, n+1)]

values = [v_0*t - 0.5*g*t**2 for t in intervals]

for i, v in zip(intervals, values):
    print("y({:.2f}) = {:.2f}".format(i, v))
