# python program to find addition of two number 
 
#  1

num1 = 20 
num2 = 30

print("addition of two number is :",num1+num2);


# 2 
num1 =int (input("enter first number:"))
num2 =int (input("enter second number:"))
sum = num1+num2
print("the addition of two number is :",sum);

# 3 

def add(num1,num2):
    sum=num1+num2;
    print("sum of two number is:", sum)

num1=eval(input("enter first number:"))
num2=eval(input("enter second number:"))
add(num1,num2);

# 4 addition program by module import

import operator

num1=eval(input("enter first number:"))
num2=eval(input("enter second number"))

sum=operator.add(num1,num2)
print(sum)

# 5 one line of code
a=5;b=6;sum=a+b;print(sum)
  
  
  
  
