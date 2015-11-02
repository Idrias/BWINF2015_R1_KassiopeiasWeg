from tkinter import *
from threading import *

root = Tk()

def mach_blau(item):
    new_button = Button()
    new_button.config(text=str(item.x_koordinate) + " " + str(item.y_koordinate), bg="light blue")
    new_button.grid(sticky=N+S+E+W, row=(item.y_koordinate-6)*-1, column=item.x_koordinate)


def build_window(liste_der_felder):
    global root
    root.geometry("700x600")

    for x in range(50):
        Grid.columnconfigure(root, x, weight=1)
    for y in range(50):
        Grid.rowconfigure(root, y, weight=1)

    for item in liste_der_felder:
        new_button = Button()
        new_button.config(text=str(item.x_koordinate) + " " + str(item.y_koordinate))

        if item.farbe == "s":
            new_button.config(bg="SlateBlue4", fg="SlateBlue4")
        if item.kassi_steht:
            new_button.config(bg="green")

        new_button.grid(sticky=N+S+E+W, row=(item.y_koordinate-6)*-1, column=item.x_koordinate)

    root.mainloop()


