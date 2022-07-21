from tkinter import*
import tkinter.messagebox as box
window = Tk()
window.Title('Mad lib story')
Frame = Frame(window)
entry=Entry(Frame)
def dialog() :
	box.showinfo('story','welcome'+ entry.get())
	btn = Button(frame,text="enter name",command=dialog)
	btn.pack(side=RIGHT,padx= 5)
	entry.pack(side=LEFT)
	frame.pack(padx = 20 ,pady =20)
	window.mainloop()


