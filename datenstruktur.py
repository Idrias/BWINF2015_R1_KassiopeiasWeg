from sys import exit
from time import sleep


class Feld(object):
    def __init__(self, farbe, x_koordinate, y_koordinate, schon_besucht):
        self.farbe = farbe
        self.x_koordinate = x_koordinate
        self.y_koordinate = y_koordinate
        self.schon_besucht = schon_besucht

        print(type(schon_besucht))
        print("Hallo ich bin ein neues Feld der Farbe ", farbe, ", meine Koordinaten sind ", x_koordinate, "/",
              y_koordinate, sep="")


def einlesen_datei(dateiname):
    try:
        datei = open(dateiname, "r")
        inhalt = datei.read()

        return inhalt
    except FileNotFoundError:
        print("Diese Datei kenne ich nicht.")
        sleep(3)
        exit()


def verarbeiten_datei(inhalt):
    x = int(inhalt[0])      # X-Koordinate auslesen, diese steht an erster Stelle
    y = int(inhalt[2])      # Y-Koordinate auslesen, folgt auf erste Stelle  + ein Leerzeichen

    while inhalt[0] is not "#":         # Alle Newlines und Leerzeichen entfernen bis zum Beginn der
        inhalt = inhalt[1:len(inhalt)]      # eigentlichen Felder

    zeilen = []             # Einzelne Zeilen der Datei in einer Liste
    aktuelle_zeile = ""         # Eine Zeile dieser Liste

    while len(inhalt) != 0:                 # Solange wir noch nicht am Ende der Datei sind
        if not inhalt[0] == "\n":           # Falls das aktuelle Zeichen nicht den Anfang einer neuen Zeile symbolisiert
            aktuelle_zeile += inhalt[0]     # Erweitere die aktuelle Zeile um das Zeichen
        else:                               #
            zeilen.append(aktuelle_zeile)
            aktuelle_zeile = ""
        inhalt = inhalt[1:len(inhalt)]

    for zeile in zeilen:
        print(zeile)



