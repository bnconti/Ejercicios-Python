# Exercise 3.18: Approximate pi

"""
SAMPLE RUN:
   2 -> 2.00000000000000000 || Margin of error: 1.14159265358979312
   4 -> 2.82842712474618985 || Margin of error: 0.31316552884360327
   8 -> 3.06146745892071781 || Margin of error: 0.08012519466907531
  16 -> 3.12144515225805153 || Margin of error: 0.02014750133174159
  32 -> 3.13654849054594065 || Margin of error: 0.00504416304385247
  64 -> 3.14033115695475429 || Margin of error: 0.00126149663503883
 128 -> 3.14127725093277999 || Margin of error: 0.00031540265701313
 256 -> 3.14151380114428846 || Margin of error: 0.00007885244550465
 512 -> 3.14157294036710866 || Margin of error: 0.00001971322268446
1024 -> 3.14158772527719332 || Margin of error: 0.00000492831259979
"""

from math import pi, sqrt, sin, cos

values = [2**k for k in range(1, 11)]
approximations = []
for n in values:
    approx = 0
    for i in range(1, n+1):
        x1 = 0.5*cos(2*pi*i/n); y1 = 0.5*sin(2*pi*i/n); x2 = 0.5*cos(2*pi*(i-1)/n); y2 = 0.5*sin(2*pi*(i-1)/n)
        approx += sqrt((x1 - x2)**2 + (y1 - y2)**2)
    approximations.append(approx)

for approx_pi, value in zip(approximations, values):
    print("{:>4} -> {:.17f} || Margin of error: {:.17f}".format(value, approx_pi, abs(pi-approx_pi)))