# Exercise 2.7: Generate equally spaced coordinates

a = 0; b = 1; n = 20; h = (b-a)/n

# coord_list = []
# for i in range(0, n+1):
#     coord_list.append(a+i*h)
# print(coord_list)

coord_list_alternative = [a+i*h for i in range(0, n+1)]
print("{} interval of length {:.2f}. Range [{};{}].".format(n, h, a, b))
for x in coord_list_alternative:
    print("{:4.2f} ".format(x), end='')

print("END.")