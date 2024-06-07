# python program to print the sum of square of first n natural number:

num=int(input("enter number from where you want to find a natural number"))
sum=0
for i in range(1,num+1):
  sum=sum+(i*i)
print("square of n natural number is :",sum)

# 2 

def squareSum(n):
  sm=0
  for i in range(1,n+1):
    sm=sm+(i*i) # sm=sm+(i*i*i)
  return sm
n=int(input("enter number:.."))
print(squareSum(n))
