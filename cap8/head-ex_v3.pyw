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

