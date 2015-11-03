from tkinter import *
from tkinter import messagebox
y_feld = 0
entrytext = ""

def zeige_nachricht(titel, text):
    messagebox.showinfo(titel, text)


def mach_farbe(farbe, item):
    new_button = Button()
    new_button.config(text=str(item.x_koordinate) + " " + str(item.y_koordinate), bg=farbe)
    new_button.grid(sticky=N+S+E+W, row=(item.y_koordinate- y_feld)*-1, column=item.x_koordinate)

def zerstoere(entry, root):
    print("ping")
    global entrytext
    entrytext = entry.get()
    root.destroy()

def erstelle_fragefenster():
     root = Tk()
     root.geometry("205x90")
     root.config(background="light green")
     Label(text=" Bitte geben sie den Dateinamen ein:", background="light green").grid(row=0, column=0)
     m_entry = Entry()
     m_entry.grid(row=1, column=0)
     Label(background="light green").grid(row=2, column=0)
     Button(text="Los gehts!",command= lambda: zerstoere(m_entry, root)).grid(row=3, column=0)
     root.mainloop()
     print(entrytext)
     return entrytext


def erstelle_fenster(liste_der_felder):

    # Erstelle TK-Window, Groesse 700x300 Pixel
    root = Tk()
    root.geometry("700x600")

    # Tabelle passt sich an vorhandenen Platz an
    for col in range(20): Grid.columnconfigure(root, col, weight=1)
    for row in range(20): Grid.rowconfigure(root, row, weight=1)

    global y_feld
    y_feld = liste_der_felder[-1].y_koordinate

    # Erstelle Buttons als Felder
    for item in liste_der_felder:
        new_button = Button()
        new_button.config(text=str(item.x_koordinate) + " " + str(item.y_koordinate))

        # Farbe des Buttons einstellen
        if item.farbe == "s": new_button.config(bg="SlateBlue4", fg="SlateBlue4")
        if item.kassi_steht: new_button.config(bg="yellow")

        # Button ans Fenster anheften, an der folgenden Stelle nach Excel-Zellenschema
        # Y-Koordinate wird hier umgewandelt, da Tkinter den Ursprung oben links setzt, ich ihn aber
        # unten links haben wollte
        print (item.y_koordinate)
        print("row=" + str((item.y_koordinate - 6) * y_feld) + " col=" + str(item.x_koordinate))
        new_button.grid(sticky=N+S+E+W, row=(item.y_koordinate - y_feld)*-1, column=item.x_koordinate)

    # Entstandenes Fenster anzeigen
    root.mainloop()



