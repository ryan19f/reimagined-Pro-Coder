from array import*
arr=array('i',[])
v=int(input("what is the length of the array"))
for i in range(v):
    x=int(input("enter the next value"))
    arr.append(x)
    print(arr)
c=int(input("enter th value for search"))
k=0
for i in arr:
        if i == c:
           flag=1
           break
        else:
           flag=0
if flag ==1:
        print("item found at position:", k + 1)
else:
         print("error")

