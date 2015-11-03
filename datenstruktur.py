from sys import exit
from time import sleep

still = 0
x_groesse = 0
y_groesse = 0


class Feld(object):
    def __init__(self, farbe, x_koordinate, y_koordinate, schon_besucht, kassi_steht):
        self.farbe = farbe  # Feldfarbe
        self.x_koordinate = x_koordinate  # X-Koordinate
        self.y_koordinate = y_koordinate  # Y-Koordinate
        self.schon_besucht = schon_besucht  # War Kassi schon hier?
        self.kassi_steht = kassi_steht  # Steht Kassi im Moment hier?

        self.verbunden = 0  # Wird bei Aufgabenteil A gleich 1 gesetzt, wenn eine Verbindung zu Kassi erkannt wird

        self.objektkoordinaten = [x_koordinate, y_koordinate]   # Koordinaten als Liste zusammengefasst

        # Ermittelt Koordinaten der benachbarten Felder
        self.nordkords = [x_koordinate, y_koordinate + 1]
        self.ostkords = [x_koordinate + 1, y_koordinate]
        self.suedkords = [x_koordinate, y_koordinate - 1]
        self.westkords = [x_koordinate - 1, y_koordinate]
        self.nachbarkoordinaten = [self.nordkords, self.ostkords, self.suedkords, self.westkords]

        # Konsoleninfo: Objekt wurde erstellt!
        self.printinfo("Neues Feld: ")

    def printinfo(self, zusatz=""):
        if not still:
            print(zusatz + "Farbe ", self.farbe, ", Koordinaten X:", self.x_koordinate, " Y:",
                  self.y_koordinate, " KassiSteht: ", self.kassi_steht, sep="")


def einlesen_datei(dateiname):
    # Datei versuchsweise oeffnen und versuchen, den Inhalt zeilenweise zu lesen
    # inhalt ist eine Liste von Strings
    try:
        datei = open(dateiname, "r")
        inhalt = datei.readlines()
        datei.close()

        # Entferne alle \n
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

    # Feldgroesse
    global x_groesse
    global y_groesse
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
            liste_neue_felder.append(Feld(farbe, index_zeichen, index_zeile, 0, kassi_steht))

    return liste_neue_felder

"""
class Loesung(object):
    def __init__(self):
        pass

def loesung_aufbereiten(zustaende, zustandsnr, vaterliste, kindliste):
    pass"""