#QUESTION 1

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))             
c=int(input("Enter the third number:"))
average=(a+b+c)/3	
print("The average of three numbers is:",average)

#QUESTION 2

a=int(input("Enter the gross income:"))
b=int(input("Enter the number of dependents:"))
tax_rate=0.20
standard_deduction=10000
dependent_deduction=3000
taxable_income=a-standard_deduction-dependent_deduction*b
tax=taxable_income*tax_rate
print("The tax is:", tax)

#QUESTION 3 

""" %= gives remainder
 // = round of result to left side of number line """
a= int(input("enter time in seconds: "))
print("time in minutes is",a//60,"minutes" ,a%60, "seconds")

#QUESTION 4

a=25
b='25'
c=25.0
print(str(a+int(b)+int(c)))

#QUESTION 5 

from math import pi,sin,cos
deg=0
y=0
z=0
for deg in range(0,346,15):
 rad= deg*(pi/180)
 y=round(sin(rad),4)
 z=round(cos(rad),4)
print("sin",deg,"=",y,"and cos",deg,"=",z)

