from tkinter import *

# Top level window 
window = Tk()

window.title("Studyfied.com")
window.geometry('350x200')

# Option menu variable
optionVar = StringVar()
optionVar.set("Red")

# Create a option menu
option = OptionMenu(window, optionVar, "Hangman", "Madlibs", "Ping-Pong")
option.pack()

# Create button with command
def show():
    print("Selected value :", optionVar.get())
    if (optionVar == Hangman):
        import hang2
    elif(optionvar ==Madlibs):
        import window
    elif(optionVar ==Ping-Pong):
        import pong
    else:
        print('Invalid choice')

btnShow = Button(window, text="Show", command=show)
btnShow.pack()

window.mainloop()
