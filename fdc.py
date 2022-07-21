nam=str(input("enter name  "))
namo=str(input("enter gender with brackets "))
num = int(input("Enter  age: "))
name = nam
namee = namo
if num >=18 and namee == "female":
   print(name + "  " +  namee + " is eligible for marriage")
elif num>=21 and namee == "male" :
   print(name +  " is eligible for marriage")
else:
   print(name +  " is not eligible for marriage")

