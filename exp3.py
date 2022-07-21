basestring=input("enter a value for base-")
base=int(basestring)
exponentstring=input("enter a value for exponent-")
exponent=int(exponentstring)
num=1
for i in range(exponent):
		num=num*base
print(num)