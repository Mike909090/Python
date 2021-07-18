from tkinter import *
# win is a top or parent window.
win = Tk()
win.geometry("300x500")
# going to make a button in the win tab and inout text that says submit  using pack() geometry.
b = Button(win, text = "Submit")
# add check button to tinker images
b.pack()
# add label to tinker images
label1 = Label(win, text="hi, welcome to GUI using Tkinter")
# using pack() to place items in the tinker frame.
label1.pack()
# making check box items
c = Checkbutton(win, text = "Python")
# add check button to tinker images
c.pack()
c1 = Checkbutton(win, text = "Java")
# add check button to tinker images
c1.pack()
c2 = Checkbutton(win, text = "SQL")
# add check button to tinker images
c2.pack()
#runs the event as long as the window is not closed.
win.mainloop()
