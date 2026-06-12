from productos import Producto

p1 = Producto("Laptop", 12000, 5)
p2 = Producto("Laptop", 12000, 3)
p3 = Producto("Mouse", 200, 2)

# Prueba de str
print(p1)
print(p2)
print(p3)

# Prueba de add
suma = p1 + p2
print(suma)

# Prueba de mul
print(p3 * 3)

# Prueba de eq
print(p1 == p2)
print(p1 == p3)

del p1
del p2
del p3
del suma