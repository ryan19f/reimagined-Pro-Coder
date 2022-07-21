lst = [5, 7, 10, 12, 15]
 
print("list of items is", lst)
 
x = int(input("enter item to search:"))
 
i = num = 0
 
while i < len(lst):
    if lst[i] == x:
        num = 1
        break
 
    i = i + 1
 
if num == 1:
    print("item found at position:", i + 1)
else:
    print("item not found")
