# maximum of two number 

# 1. 

a=4
b=3
if(a>b):
  print("this number is maximum number between teo number:",a)
else:
  print("this number is maximum number between teo number:",b)
  
# 2.

num1=eval(input("enter a first number:"))
num2=eval(input("enter second number : "))

if(num1>num2):
  print(num1," is maximum between two given number ")
  
else:
  print(num2,"is maximum between two given number ")
  
# 3.
 
def maximum(num1,num2):
  if(num1>num2):
    return num1
  else:
    return num2
num1=30
num2=20
print(maximum(num1,num2))
print("is the maximum number:")

# 4.  by max function

a = 2
b = 4
 
maximum = max(a, b)
print(maximum)

# 5.  python code to find maximum of two numbers by lambda function
 
a=2;b=4
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')