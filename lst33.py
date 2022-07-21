def lin(x): 
    print("list of items is", lst)
     
    x = int(input("enter item to search:"))
     

     
    for i in lst:
        if i == x:
            print("item is present")
        else:
            print("error")


lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lin(lst))








    

 
