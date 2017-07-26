"""
Exercise 1.4: Convert from meters to British length units
Make a program where you set a length given in meters and then compute and write
out the corresponding length measured in inches, in feet, in yards, and in miles. Use
that one inch is 2.54 cm, one foot is 12 inches, one yard is 3 feet, and one British
mile is 1760 yards. For verification, a length of 640 meters corresponds to 25196.85
inches, 2099.74 feet, 699.91 yards, or 0.3977 miles.
Filename: length_conversion
"""

lenght_meters = 640

lenght_inches = (lenght_meters*100)/2.54
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