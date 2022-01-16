# Phython program to find the are of triangle

# Take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c)/2

#calculating the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is %0.2f" %area)
input("press ant key to exit...")


