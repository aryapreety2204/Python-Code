# The Fibonacci sequence is a type series where each number is the sum of the two that precede it. It starts from 0 and 1 usually. The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. 


# 1 
num=int(input("how many term would you find .....: "))

count =0
n1=0;n2=1
if(num<=0):
  print("please enter a positive number :.....")
elif(num==1):
  print("the fibonacci series upto",num)
  print(n1)
else:
  print("fibonacci sequence is:....")
  
  while count<num:
    print(n1)
    nth=n1+n2
    # update value
    n1=n2
    n2=nth
    count+=1
    
    
# 2  Function to find the nth Fibonacci number using Python

def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


# Driver Program
n=int(input("how many enter...?"))
print(Fibonacci(n))

  
    
    