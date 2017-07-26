# Exercise 1.4: Convert from meters to British length units

"""
SAMPLE RUN:
ORIGINAL LENGHT: 640.00 METERS.
25196.85 INCHES.        
2099.74 FEET.          
699.91 YARDS.
0.40 MILES.
"""

lenght_meters = 640

lenght_inches = lenght_meters*100/2.54
lenght_feet = lenght_inches/12.0
lenght_yard = lenght_feet/3.0
lenght_miles = lenght_yard/1760.0

print ("""\
ORIGINAL LENGHT:  {:.2f} METERS.
{:.2f} INCHES.        
{:.2f} FEET.          
{:.2f} YARDS.
{:.2f} MILES.
""".format(lenght_meters, lenght_inches, lenght_feet, lenght_yard, lenght_miles))
