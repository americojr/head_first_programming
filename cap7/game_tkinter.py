#Versao do gameshow utilizando GUI

from tkinter import *

app = Tk()
app.title("Your tkinter application")
app.geometry("450x100+200+100")
b1 = Button(app, text = "Top", width = 10)
b1.pack(side = 'top')
b2 = Button(app, text = "Bottom", width = 10)
b2.pack(side = 'bottom')
b3 = Button(app, text = "Right", width = 10)
b3.pack(side = 'right')
b4 = Button(app, text = "Left", width = 10)
b4.pack(side = 'left')


app.mainloop()

#, padx = 10, pady = 10
