print("welcome to Clement's Annuity plan Calculator")
input("press ant key to continue")

PMT = int(input("Please input regulat payment(N): "))
R = int(input("Please input annual rate(%): "))
n = int(input("Please input number of compounding periods per year: "))
t = int(input("Please input number of years: "))

u = (1 + ((R/100)/n))
v= u**(n*t)

w= v -1

y = w/((R/100)/n)

z=PMT * y

A = z

print("Your total amount is",A,"with",A-PMT,"as your interest")
input("press any key to continue")
