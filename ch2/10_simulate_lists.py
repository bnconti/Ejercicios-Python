# Exercise 2.10: Simulate operations on lists by hand
"""
a = [1, 3, 5, 7, 11]    #  CREATES LIST a WITH SOME VALUES
b = [13, 17]            #  CREATES LIST b WITH SOME VALUES
c = a + b               #  GENERATES THE LIST C, CONTAINING THE SUM BETWEEN a AND b.
print(c)                #  PRINTS c.
b[0] = -1               #  DEFINES THE ELEMENT 0 TO -1
d = [e+1 for e in a]    #  GENERATES A NEW LIST d WITH ALL THE VALUES FROM a + 1
print(d)                #  PRINTS d.
d.append(b[0] + 1)      #  APPENDS 0 AT d.
d.append(b[-1] + 1)     #  APPENDS 18 AT d.
print(d[-2:])           #  PRINTS d STARTING FROM 13.
for e1 in a:            #  FOR EACH ELEMENT IN a...
    for e2 in b:        #  FOR EACH ELEMENT IN b...
        print(e1 + e2)  #  PRINT THE SUM OF e1 AND e2.
"""
