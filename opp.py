a=input("Enter first numbers:    ")
b=input("Enter second numbers:    ")
print("\nMenu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=input("enter choice:    ")
switcher = { 
        0: res = a + b,
        1: res = a - b, 
        2: res = a * b, 
	3: res = a / b
    } 
return switcher.get(argument, "nothing") 
  
