from tkinter import*
window = Tk()
window.title('label example ')
adjective1 = input("Tell me an adjective, and click enter. ")
noun1 = input("Tell me a noun (plural), and click enter. ")
adjective2 = input("Tell me an adjective, and click enter. ")
noun2 = input("Tell me another noun, and click enter. ")
verb = input("Tell me a verb, and click enter. ")
print ('\n'"There was once a "+ adjective1 +" boy from Dubai"'\n'"who was baked by "+ noun1 + " in a pie"'\n'" to his "+ noun2 + "'s " + adjective2 + " disgust "'\n'"he "+ verb +" through the crust"'\n'"and exclaimed ,'what a good boy am I !'"'\n'"so are you happy with your wacky story!")
label=Label(window,text ="There was once a "'\n'" boy from Dubai he was eating pie in mumbai")
label.pack(padx = 200,pady = 50)
