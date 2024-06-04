# python program to find prime number in given length...

start = int(input("enter stating number:..."))
end = int(input("enter end number:...."))

print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
# all prime numbers are greater than 1
     if num > 1:
        for a in range(2, num):
          if (num % a) == 0:
            break
        else:
          print(num)
          
# 2 the python to check prime number 

num=int(input("enter a number:"))
if(num>1): 
  for i in range(2,int(num/2)+1): 
    if(num%i==0):
      print(num,"is not a prime number..:")
      break
    else:
      print(num,"is a prime number")
else:
  print(num,"is not prime number")


