# subtraction program 
 
 # 1. one line of code 
 
a=2;b=1;sub=a-b;print(sub)

# 2. 

num1=eval(input("enter first number :"))
num2=eval(input("enter second number:"))

sub=num1-num2
print("subtraction of two number is :",sub)

# 3

def subtraction(num1,num2):
  sub=num1-num2
  print("subtraction of two number is :",sub)
  return sub
num1=eval(input("enter first number:"))
num2=eval(input("enter second number:"))
subtraction(num1,num2)

# 4 subtaction program by operators 

import  operator
num1=34
num2=20
sub=num1-num2
sub=operator.sub(num1,num2)
print(sub)

# 5. 
import  operator
num1=eval(input("enter first number:"))
num2=eval(input("enter second number:"))

sub =num1-num2
sub=operator.sub(num1,num2)
print("subtraction of two number is :",sub)
