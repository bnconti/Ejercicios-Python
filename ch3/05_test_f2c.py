# Exercise 3.5: Write a test function for Exercise 3.4

"""
SAMPLE RUN:
  0.0 ==   0.0? True
 10.0 ==  10.0? True
 20.0 ==  20.0? True
 30.0 ==  30.0? True
 40.0 ==  40.0? True
 50.0 ==  50.0? True
 60.0 ==  60.0? True
 70.0 ==  70.0? True
 80.0 ==  80.0? True
 90.0 ==  90.0? True
100.0 == 100.0? True
110.0 == 110.0? True
-20.0 == -20.0? True
-10.0 == -10.0? True
  0.0 ==   0.0? True
 10.0 ==  10.0? True
 20.0 ==  20.0? True
 30.0 ==  30.0? True
 40.0 ==  40.0? True
 50.0 ==  50.0? True
 60.0 ==  60.0? True
 70.0 ==  70.0? True
 80.0 ==  80.0? True
 90.0 ==  90.0? True
"""

c_test_values = [i for i in range(0, 120, 10)]
f_test_values = [i for i in range(-20, 100, 10)]


def test_F_C():
    c_converted_values = [C(F(c)) for c in c_test_values]
    f_converted_values = [F(C(f)) for f in f_test_values]

    for c, cp in zip(c_test_values, c_converted_values):
        print("{:5.1f} == {:5.1f}? {}".format(c, cp, c-cp < 1E-14))
    for f, fp in zip(f_test_values, f_converted_values):
        print("{:5.1f} == {:5.1f}? {}".format(f, fp, f-fp < 1E-14))


def C(f):
    c = 5/9*(f - 32)
    return c


def F(c):
    f = 9/5*c + 32
    return f

test_F_C()
