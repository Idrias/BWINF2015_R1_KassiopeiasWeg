from sys import exit
from time import sleep


class Feld(object):
    def __init__(self, farbe, x_koordinate, y_koordinate, schon_besucht, kassi_steht, mute=0):

        self.farbe = farbe                      # Feldfarbe
        self.x_koordinate = x_koordinate        # X-Koordinate
        self.y_koordinate = y_koordinate        # Y-Koordinate
        self.schon_besucht = schon_besucht      # War Kassi schon hier?
        self.kassi_steht = kassi_steht          # Steht Kassi im Moment hier?

        #
        # Konsoleninfo: Objekt wurde erstellt!
        if not mute:
            print("Neues Feld: Farbe ", farbe, ", Koordinaten X:", x_koordinate, " Y:",
                  y_koordinate, sep="")


def einlesen_datei(dateiname):
    # Datei versuchsweise oeffnen und versuchen, den Inhalt zeilenweise zu lesen
    # Inhalt ist eine Liste von Strings
    try:
        datei = open(dateiname, "r")
        inhalt = datei.readlines()
        datei.close()

        for index, line in enumerate(inhalt):
            inhalt[index] = line.rstrip()

        return inhalt

    # Datei wurde nicht gefunden (Vermutlich falscher Name angegeben)
    except FileNotFoundError:
        print("Diese Datei kenne ich nicht.")
        sleep(3)
        exit()


def verarbeiten_datei(inhalt):
    # Ziel ist es, jedes ausgelesene Zeichen in ein Objekt der Klasse Feld
    # umzuwandeln. Diese Objekte sollen in der Liste liste_neue_felder gespeichert werden.
    liste_neue_felder = []

    # Feldgroesse - WIRD IM MOMENT NICHT BEACHTET!
    x_groesse = inhalt[0][0]
    y_groesse = inhalt[0][2]

    # Zeile, die die Groesseninformation enthaelt entfernen und Liste umkehren,
    # damit der Koordinatenursprung im SuedWesten liegt
    inhalt = inhalt[1:len(inhalt)]
    inhalt = list(reversed(inhalt))

    # Fuer jedes Zeichen in jeder Zeile soll ein Objekt angelegt werden
    for index_zeile, zeile in enumerate(inhalt):
        for index_zeichen, zeichen in enumerate(zeile):
            if zeichen is "#":
                farbe = "s"
            else:
                farbe = "w"

            if zeichen is "K":
                kassi_steht = 1
            else:
                kassi_steht = 0

            # Erstelle neues Objekt. X-Koord. ist der Index des Zeichens in der Zeile (von links),
            # Y-Koord ist Nummer der Zeile (von unten).
            liste_neue_felder.append(Feld(farbe, index_zeichen, index_zeile, 0, kassi_steht, 1))
