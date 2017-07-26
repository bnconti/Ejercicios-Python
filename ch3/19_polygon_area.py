# Exercise 3.19: Compute the area of a polygon


def polygon_area(x, y):
    A = 0; i = 1
    while i <= (len(x)-1):
        A += x[i-1]*y[i] - y[i-1]*x[i]
        i += 1
    return abs(0.5*A)

triangle = [[0,0,3], [0, 4, 0]]
quadrylateral = [[0, 0, 3, 3], [0, 4, 4, 0]]
pentagon = [[1, 3, 4, 2, 0], [0, 0, 2, 3, 2]]

print(polygon_area(triangle[0], triangle[1]))
print(polygon_area(quadrylateral[0], quadrylateral[1]))
print(polygon_area(pentagon[0], pentagon[1]))