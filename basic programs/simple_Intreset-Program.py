# simple interest program from different  type's:

principle=eval(input("enter principle of Amount  :  "))
rate =eval(input("enter rate of Amount  :  "))
time = eval(input("enter the time of Amount  :  "))

SI = (principle*rate*time)/100
print("the Simple Interest of given ",principle," is : ", SI)

# 2
def SI(principle,rate,time):
  si = (principle*rate*time)/100
  print("simple interest of",principle,"is :",si)
principle=eval(input("enter principle of Amount  :  "))
rate =eval(input("enter rate of Amount  :  "))
time = eval(input("enter the time of Amount  :  "))
SI(principle,rate,time)

# 3  

def SI (p,r,t):
    si = (p*r*t)/100 ;print("the SI of given amount is :  ",si); 
p = eval(input("enter the a amount of principle:  ")); 
r=eval(input("enter the amount of rate:  ")) ;
t= eval (input("enter the time of amount:  "))
SI(p,r,t)



