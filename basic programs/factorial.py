# factorial program by some different methods 
num=int(input("enter any number:"))
fact=1
if(num<0):
  print("sorry factorial does'not exists:")
elif num==0:
  print("factorial of ) is 1 :")
else:
  for i in range(1,num+1,1):
    fact=fact*i
print("factorial of ",num," is ",fact)  
  
  
  # 2 
  
def factorial(num):
  fact=1
  if(num<0):
    print("sorry the factorial of",num,"is not exists:")
  elif(num==0):
    print("the factorial",num, "is 1..:")
  else:
    for i in range(1,num+1,1):
      fact=fact*i
  print("the factorial of the",num,"is",fact)
  
num=int(input("enter that number whose factorial is find :   "))
factorial(num)

# 3   one line code for factorial find 

def factorial(n):
  return 1 if(n==0 or n==1) else n*factorial(n-1)
n=int(input("enter the number whose factorial is finding....   :"))
print("factorial of given number is",n,":",factorial(n))


