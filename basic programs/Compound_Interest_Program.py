# python program for compound Interest in different way's

# 1 

principle = eval(input("enter principle amount:...."))
Rate = eval(input("enter rate of amount :...."))
Time = eval(input("enter time of amount :...."))

Amount=principle*(pow(1+(Rate/100),Time))
CI = Amount-principle
print("Compound Interest is :......",CI)


# 2 

principle = 50000
Rate = 5
Time = 2

Amount=principle*(pow(1+(Rate/100),Time))
CI = Amount-principle
print("Compound Interest is :......",CI)

# 3 

def Compound_Interest(p,r,t):
  Amount = p*(pow(1+(r/100),t))
  CI = Amount-p
  print("Compound_Interest is :....",CI)
Compound_Interest(50000,2,1)

# 4 
def Compound_Interest(p,r,t):
  Amount = p*(pow(1+(r/100),t))
  CI = Amount-p
  print("Compound_Interest is :....",CI)
p=eval(input("enter the principle amount:...."))
r=eval(input("enter the rate of amount:...."))
t=eval(input("enter the time of amount:..."))
Compound_Interest(p,r,t)

# 5 
def CI(p,r,t):
  amount=p*(pow(1+(r/100),t));ci=amount-p;return ci
print("compound Interest is...:",CI(5000,2,1))





  


