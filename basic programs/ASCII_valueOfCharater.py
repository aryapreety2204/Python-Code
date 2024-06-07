# program to print Ascii value of character:...
char = input("enter a character whose ascii code you want to find...")
print("the ASCII value of"+ char +"is",ord(char))

# by function
def character(char):
  print("ASCII code of the "+char+" is",ord(char))
  return char
char=input("enter the character whose code you want to find:....")
character(char)


# one line code
char=input("enter a character..:");print("the ASCII code of"+char+"is",ord(char))