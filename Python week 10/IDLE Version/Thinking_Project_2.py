# solve the quadratic equatin ax**2 + bx + c =0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant

d = (b**2)- (4*a*c)

#find the soutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print ('The solution are', sol1,"and",sol2)
input("press ant key to exit...")
