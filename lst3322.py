lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print("list of items is", lst)
x = int(input("enter item to search:"))
for i in lst:
        if i == x:
           flag=1
           break
        else:
           flag=0
if flag ==1:
         print("item is present")
else:
         print("error")




    

 
