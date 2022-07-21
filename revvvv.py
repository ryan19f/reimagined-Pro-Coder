def rev1(string):
    if len(string)==0:
        return
    temp=string[0]
    rev1(string[1:])
    print(temp,end="")


string=str(input(""))
rev1(string)
