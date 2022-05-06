QUESTION 1

str="python is a case sensitive language"
print(len(str))
rev=str[::-1]
print(rev)
new_str=str[10:26]
print(new_str)
obj=str.replace('case sensitive language',"object oriented")
print(obj)
idx=(str.index("a"))
print(idx)
spc=str.replace(" ","")
print(spc)

QUESTION 2

string="Hey,PARTH JAIN Here"
print(string)
string="My SID is 21109004"
print(string)
string="I am from production department and my CGPA is 9.9"
print(string)

QUESTION 3

#bitwise operators
a=56
b=10
print("a&b:",a&b)
print("a|b:",a|b)
print("a^b:",a^b)
print("a<<2:",a<<2)
print("b<<2:",b<<2)
print("a>>2:",a>>2)
print("b>>4:",b>>4)

QUESTION 4

input_string=input("Enter the string: ")
check_name=input_string.find("name")
if(check_name==-1):
    print("NO")
else:
    print("YES")

QUESTION 5

side_1=int(input("Enter the side 1: "))
side_2=int(input("Enter the side 2: "))
side_3=int(input("Enter the side 3: "))

a=side_1 + side_2
b=side_2 + side_3
c=side_3 + side_1

x= (side_1 < b)
y= (side_2 < c)
z= (side_3 < a)

answer = str(x & y & z)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")
print(answer)

QUESTION 6

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
n=a^b
count=0
while n:
    count+=1
    n&=(n-1)

print("Required number of bits to be flipped:",count)
