# Exercício do Caítulo 8 - Programa para registros de entregas da Head-Ex 

from tkinter import *
import tkinter.messagebox


def save_data():
    try:
        file = open("deliveries_v2.txt","a")
        file.write("Depot: \n %s \n" % depot.get())
        file.write("Description: \n %s \n" % description.get())
        file.write("Address: \n %s \n" % address.get("1.0",END))
    #   depot.delete(0,END)
        depot.set(None)
        description.delete(0,END)
        address.delete("1.0",END)
        file.close()
    except Exception as ex:
        tkinter.messagebox.showerror("Error!","Can't write to the file \n %s" % ex)

def read_depots(file):
    dpots = []
    depots_f = open(file)
    for line in depots_f:
        depot = line.rstrip()
        dpots.append(depot)
    depots_f.close()
    return dpots


app = Tk()
app.title("Head-Ex Deliveries")

#depots = ["Cambridge, MA", "Cambridge, UK", "Seattle, WA"]

Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()


app.mainloop()

