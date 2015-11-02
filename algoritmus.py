# BlaBla
import fenster
from time import sleep


def finde_kassi(objektliste):
    for item in objektliste:
        if item.kassi_steht:
            item.printinfo("Gefundenes Feld: ")
            return item


def suche_verbindungen(objektliste, aktuelles_feld):
    # Verbindungen können N,S,W,O sein!
    liste_verbundener_felder = []

    for objekt in objektliste:
        objektx = objekt.x_koordinate
        objekty = objekt.y_koordinate
        objektkoordinaten = [objektx, objekty]

        if objektkoordinaten in aktuelles_feld.nachbarliste:
            if objekt.farbe == "w" and objekt.verbunden == 0:
                objekt.printinfo("", 1)
                objekt.verbunden = 1
                liste_verbundener_felder.append(objekt)

    return liste_verbundener_felder


def verbindungstest(objektliste):
    aktuelles_feld = finde_kassi(objektliste)
    aktuelles_feld.verbunden = 1
    verbundene_felder = suche_verbindungen(objektliste, aktuelles_feld)

    anzahl_verbundene = 1 + len(verbundene_felder)
    anzahl_weisse = 0

    for objekt in objektliste:
        if objekt.farbe == "w":
            anzahl_weisse += 1

    while len(verbundene_felder) != 0:
        neu_gefundene = []

        for feld in verbundene_felder:
            fenster.mach_blau(feld)
            aktuelles_feld = feld
            neu_gefundene += suche_verbindungen(objektliste, aktuelles_feld)
        sleep(0.5)

        anzahl_verbundene += len(neu_gefundene)
        verbundene_felder = neu_gefundene

    print(anzahl_weisse, anzahl_verbundene)
    if anzahl_weisse == anzahl_verbundene:
        print("TADA!!!")

        # besuchte felder werden zu stein - jedes mal neu erreichbarkeit aller felder pruefen!

