"""
Exercise 1.5: Compute the mass of various substances
The density of a substance is defined as % D = m/V , where m is the mass of a volume
V . Compute and print out the mass of one liter of each of the following substances
whose densities in g/cm 3 are found in the file src/files/densities.dat 6 : iron,
air, gasoline, ice, the human body, silver, and platinum.
Filename: 1liter.
"""

LITER = 1000.0

D_iron = LITER*7.8
D_air = LITER*0.0012
D_gasoline = LITER*0.67
D_ice = LITER*0.9
D_human_body = LITER*1.03
D_silver = LITER*10.5
D_platinum = LITER*21.4

print("""\
== DENSITY IN 1 LITER == 

IRON:           {:.2f}
AIR:            {:.2f}
GASOLINE:       {:.2f}
ICE:            {:.2f}
HUMAN BODY:     {:.2f}
SILVER:         {:.2f}
PLATINUM:       {:.2f}
""".format(D_iron, D_air, D_gasoline, D_ice, D_human_body, D_silver, D_platinum))