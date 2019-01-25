#Versao do gameshow utilizando GUI

from tkinter import *
import play_music


def play_correct_sound():
    ncorretas.set(ncorretas.get() + 1)
    play_music.play("correct.wav")


def play_wrong_sound():
    nerradas.set(nerradas.get() + 1)
    play_music.play("wrong.wav")


app = Tk()
app.title("TVN Game Show")
app.geometry("300x100+200+100")

ncorretas = IntVar()
ncorretas.set(0)
nerradas = IntVar()
nerradas.set(0)

l = Label(app, text = "When you are ready, click on the button!", height = 3)
l.pack()

cont_c = Label(app, textvariable = ncorretas)
cont_c.pack(side = "left")

cont_e = Label(app, textvariable = nerradas)
cont_e.pack(side = "right")

b1 = Button(app, text = "Correct!", width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()

