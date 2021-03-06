# Exercício do Caítulo 8 - Programa para registros de entregas da Head-Ex 

from tkinter import *

def save_data():
    file = open("deliveries_v2.txt","a")
    file.write("Depot: \n %s \n" % depot.get())
    file.write("Description: \n %s \n" % description.get())
    file.write("Address: \n %s \n" % address.get("1.0",END))
#   depot.delete(0,END)
    depot.set(None)
    description.delete(0,END)
    address.delete("1.0",END)
    file.close()


app = Tk()
app.title("Head-Ex Deliveries")

Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)
Radiobutton(app, text = "Cambridge, MA", value = "Cambridge, MA", variable = depot).pack()
Radiobutton(app, text = "Cambridge, UK", value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text = "Seattle, WA", value = "Seattle, WA", variable = depot).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()


app.mainloop()

