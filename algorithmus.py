import copy
import fenster
import datenstruktur
from time import sleep
from sys import exit


def finde_anzahl_weisse_felder(objektliste):
    anzahl_weisse = 0
    for objekt in objektliste:
        if objekt.farbe == "w":
            anzahl_weisse += 1
    return anzahl_weisse


def finde_kassi(objektliste):
    for item in objektliste:
        if item.kassi_steht:
            item.printinfo("Kassi steht hier: ")
            return item


def suche_verbindungen(objektliste, aktuelles_feld):
    # Verbindungen k�nnen im N,S,W oder O sein!
    liste_verbundener_felder = []  # Eine Liste aller weissen Felder die an das
    # untersuchte Feld angrenzen und noch nicht als verbunden erkannt
    # wurden
    for objekt in objektliste:
        if objekt.objektkoordinaten in aktuelles_feld.nachbarkoordinaten:
            # Das angeschaute Objekt ist ein Nachbar des untersuchten Feldes
            if objekt.farbe == "w" and objekt.verbunden == 0:
                # Die Farbe ist weiss und es ist bisher noch nicht als Verbindung erkannt worden
                #objekt.printinfo("(In)direkte Verbindung zu Kassi: ")
                objekt.verbunden = 1
                liste_verbundener_felder.append(objekt)
    return liste_verbundener_felder


def verbindungstest(farbe, objektliste):

    aktuelles_feld = finde_kassi(objektliste)  # Wir beginnen unsere Suche auf Kassis aktuellen Feld
    aktuelles_feld.verbunden = 1  # Dieses ist natuerlich verbunden

    # Wir finden heraus, welche weissen Felder mit Kassis Feld verbunden sind, die noch nicht als verbunden
    # erkannt wurden
    verbundene_felder = suche_verbindungen(objektliste, aktuelles_feld)
    for feld in verbundene_felder:
        if farbe: fenster.mach_farbe("light green", feld)


    # Kassis Feld selbst ist verbunden, dazu alle jetzt neu gefundenen verbundenen Felder
    anzahl_verbundene = 1 + len(verbundene_felder)

    # Wir finden heraus wie viele weisse Felder es insgesamt in Quadratien gibt
    anzahl_weisse = finde_anzahl_weisse_felder(objektliste)

    # So lange wir noch neue verbundene Felder finden
    while len(verbundene_felder) != 0:

        # Liste der Felder, die widerum an die eben schon gefundenen angrenzen
        neu_gefundene = []

        # Fuer jedes der eben gefundenen Felder wird widerum eine Untersuchung auf unbekannte, weisse
        # Nachbarfelder durchgef�hrt
        for feld in verbundene_felder:

            if farbe: fenster.mach_farbe("light green", feld)
            aktuelles_feld = feld

            neu_gefundene += suche_verbindungen(objektliste, aktuelles_feld)

        if farbe: sleep(0.0)

        anzahl_verbundene += len(neu_gefundene)  # Anzahl der insgesamt verbundenen weissen Felder wird
        # entsprechend erhoeht

        verbundene_felder = neu_gefundene  # Die neu gefundenen werden wieder zu den verbundenen feldern
        # und die Suche kann weitergehen


   # print("Es gibt " + str(anzahl_weisse) + " weisse Felder, davon sind " + str(
   #     anzahl_verbundene) + " miteinander verbunden!")

    if anzahl_weisse == anzahl_verbundene:
        if farbe: fenster.zeige_nachricht("Super!", "Alle weissen Felder sind für Kassi erreichbar.")
        print(1)
        return 1
    else:
        if farbe: fenster.zeige_nachricht("Schade", "Kassi kann leider nicht alle Felder erreichen. :-(")
        return 0

        # besuchte felder werden zu stein - jedes mal neu erreichbarkeit aller felder pruefen!


def kassi_bewedi(objektliste, kassi_anfang, kassi_ende):
    kopierte_objektliste = copy.deepcopy(objektliste)

    for index, item in enumerate(kopierte_objektliste):
        if item.objektkoordinaten == kassi_anfang.objektkoordinaten:
            kopierte_objektliste[index].kassi_steht = 0
            kopierte_objektliste[index].farbe = "s"
            kopierte_objektliste[index].schon_besucht = 1
            #fenster.mach_farbe("black", item)

        if item.objektkoordinaten == kassi_ende.objektkoordinaten:
            kopierte_objektliste[index].kassi_steht = 1
            kopierte_objektliste[index].schon_besucht = 1

    return kopierte_objektliste


def unverbind(liste):
    for index, item in enumerate(liste):
        liste[index].verbunden = 0


def kassi_finde_weg(objektliste):
    zustaende = [objektliste]
    vaterliste = []
    kindliste = []
    loesungen = []
    history = []

    for zustandsnr, zustand in enumerate(zustaende):
        print("STARTE ZUSTAND " + str(zustandsnr))
        unverbind(zustand)
        print("U1 " + str(zustandsnr))
        if not verbindungstest(0, zustand):
            print("U2 " + str(zustandsnr))
            print("Kassi hat sich den Weg in Zustand " + str(zustandsnr) + " versperrt.")
            #continue
        print("U3 " + str(zustandsnr))
        unverbind(zustand)
        print("U4 " + str(zustandsnr))
        for item in zustand:
            item.printinfo()
        print("U5 " + str(zustandsnr))
        moegliche_ziele = suche_verbindungen(zustand, finde_kassi(zustand))
        print("U6 " + str(zustandsnr))

        for ziel in moegliche_ziele:
            neuer_zustand = kassi_bewedi(zustand, finde_kassi(zustand), ziel)
            zustaende.append(neuer_zustand)

            print("Zustand " +str(zustandsnr) + " ("+str(finde_kassi(zustand).objektkoordinaten)+")"+" kann nach " + str(ziel.objektkoordinaten))
            print("Kind: " + str(len(zustaende)-1))
            print()

            vaterliste.append(zustandsnr)
            kindliste.append(len(zustaende) - 1)

        print(finde_anzahl_weisse_felder(zustand))
        if finde_anzahl_weisse_felder(zustand) == 1:
            print(zustandsnr)
            print("Keine weissen Felder verbleibend!")
            print(vaterliste)
            print(kindliste)
            print()

            gesuchte_nummer = zustandsnr
            gesucht = "kind"

            #while gesuchte_nummer != 0:
            for vaternummer, kindnummer in zip(reversed(vaterliste), reversed(kindliste)):
                if vaternummer == gesuchte_nummer and gesucht == "vater":
                    gesuchte_nummer = kindnummer
                    gesucht = "kind"
                    history.append(vaternummer)
                if kindnummer == gesuchte_nummer and gesucht == "kind":
                    gesuchte_nummer = vaternummer
                    gesucht = "kind"
                    history.append(kindnummer)
            loesungen.append(history)

            for item in zustaende[0]:
                if item.kassi_steht:
                    letztes_objekt = item

            himmelsrichtungen = ""
            for item in list(reversed(history)):
                for thing in zustaende[item]:
                    if thing.kassi_steht:
                        fenster.mach_farbe("yellow", thing)
                        fenster.mach_farbe("gray", letztes_objekt)

                        #sleep(0.5)
                        if thing.objektkoordinaten == letztes_objekt.nordkords:
                            himmelsrichtungen += " N "
                        elif thing.objektkoordinaten == letztes_objekt.ostkords:
                            himmelsrichtungen += " O "
                        elif thing.objektkoordinaten == letztes_objekt.suedkords:
                            himmelsrichtungen += " S "
                        elif thing.objektkoordinaten == letztes_objekt.westkords:
                            himmelsrichtungen += " W "
                        letztes_objekt = thing
            fenster.zeige_nachricht("Himmelsrichtungen", "Der eben gezeigte Loesungsweg verlaeuft so:\n" + himmelsrichtungen)

            print("Das ist eine Loesung!")
            print(len(loesungen))
            print(himmelsrichtungen)
            history = []
        print("Zustand: " +str(zustandsnr)+ " von " + str(len(zustaende)-1))
    print("das ende aller zustaende ist.. erreicht")

    if not loesungen:
        fenster.zeige_nachricht("Das Ende aller Dinge", "Leider gibt es keine Loesungsmoeglichkeit fuer Aufgabenteil B.")
    else:
        fenster.zeige_nachricht("Das Ende aller Dinge", "Sie haben jetzt alle " +str(len(loesungen))+ " Loesungsmoeglichkeiten gesehen.")
    print(len(loesungen))



    #print(history)








