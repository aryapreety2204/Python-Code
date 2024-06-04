# Area of circle program

# 1. 
radius = eval(input("enter a radius of circle:..."));
Area = radius*radius*3.14
print(Area," is the area of circle....")

# 2 
import operator
def Area(r):
  area=operator.mul(r,r)*3.14;return area
print(Area(2),"is the area of circle:....")

# 3 
import operator
r=eval(input("enter a radius:..")); area=operator.mul(r,r)*3.14; print(area,"is the radius of circle")

# 4 
def Area(r):
  area=r*r*3.14;return area
r=eval(input("enter the radius of circle:"))
print(Area(r),"is the area of circle")
