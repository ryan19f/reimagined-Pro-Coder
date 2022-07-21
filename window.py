from tkinter import *
adjective1 = input("Tell me an adjective, and click enter. ")
noun1 = input("Tell me a noun (plural), and click enter. ")
adjective2 = input("Tell me an adjective, and click enter. ")
noun2 = input("Tell me another noun, and click enter. ")
verb = input("Tell me a verb, and click enter. ")
title =('Welcome to Mad libs Lets start')
print (title)
master = Tk()
master.title('Mad Libs')
x = adjective1
y = noun1
z = adjective2
a = noun2
b = verb
master.minsize(width=400, height=400)
w = Label(master, text="There was once a "+ x +" boy from Dubai"'\n'"who was baked by "+ y + " in a pie"'\n'" to his "+ z + "'s " + a+ " disgust "'\n'"he "+ b+" through the crust"'\n'"and exclaimed ,'what a good boy am I !'"'\n'"so are you happy with your wacky story!" )
w.pack()
mainloop()
