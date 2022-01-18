print("Welcome to Clement's Compound Interest Calculator")
input("press any key to continue...")

#Variables for calculating
P = int(input("Please input principle(N): "))
R = int(input("Please input interest rate(%): "))
n = int(input("Please input number of compounds per year: "))
t = int(input("Please input number of years: "))

#formula
x = (1 + ((R/100)/n))
z = x**(n*t)

A = P * z
#output
print("Your total amount is",A,"with",A-P,"as your interest")
input("press any key to continue...")
