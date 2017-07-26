# Exercise 3.19: Compute the area of a polygon

"""
SAMPLE RUN:
Area of the triangle with vertices x[0, 0, 3], y[0, 4, 0]: 6.0
Area of the quadrilateral with vertices x[0, 0, 3, 3], y[0, 4, 4, 0]: 12.0
Area of the pentagon with vertices x[1, 3, 4, 2, 0], y[0, 0, 2, 3, 2]: 9.0
"""

def polygon_area(x, y):
    A = 0; i = 1
    while i <= (len(x)-1):
        A += x[i-1]*y[i] - y[i-1]*x[i]
        i += 1
    return abs(0.5*A)

triangle = [[0, 0, 3], [0, 4, 0]]
quadrilateral = [[0, 0, 3, 3], [0, 4, 4, 0]]
pentagon = [[1, 3, 4, 2, 0], [0, 0, 2, 3, 2]]

print("Area of the triangle with vertices x{}, y{}: {}"
      .format(triangle[0], triangle[1],polygon_area(triangle[0], triangle[1])))
print("Area of the quadrilateral with vertices x{}, y{}: {}"
      .format(quadrilateral[0], quadrilateral[1], polygon_area(quadrilateral[0], quadrilateral[1])))
print("Area of the pentagon with vertices x{}, y{}: {}"
      .format(pentagon[0], pentagon[1], polygon_area(pentagon[0], pentagon[1])))
