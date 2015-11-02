import copy

def finde_kassi(objektliste):
    for item in objektliste:
        if item.kassi_steht:
            item.printinfo("Kassi steht hier: ")
            return item


def suche_verbindungen(objektliste, aktuelles_feld):
    # Verbindungen können im N,S,W oder O sein!

    liste_verbundener_felder = []  # Eine Liste aller weissen Felder die an das
    # untersuchte Feld angrenzen und noch nicht als verbunden erkannt
    # wurden

    for objekt in objektliste:
        if objekt.objektkoordinaten in aktuelles_feld.nachbarkoordinaten:
            # Das angeschaute Objekt ist ein Nachbar des untersuchten Feldes
            if objekt.farbe == "w" and objekt.verbunden == 0:
                # Die Farbe ist weiss und es ist bisher noch nicht als Verbindung erkannt worden
                objekt.printinfo("(In)direkte Verbindung zu Kassi: ")
                objekt.verbunden = 1
                liste_verbundener_felder.append(objekt)

    return liste_verbundener_felder


def verbindungstest(objektliste):
    aktuelles_feld = finde_kassi(objektliste)  # Wir beginnen unsere Suche auf Kassis aktuellen Feld
    aktuelles_feld.verbunden = 1  # Dieses ist natuerlich verbunden

    # Wir finden heraus, welche weissen Felder mit Kassis Feld verbunden sind, die noch nicht als verbunden
    # erkannt wurden
    verbundene_felder = suche_verbindungen(objektliste, aktuelles_feld)

    # Kassis Feld selbst ist verbunden, dazu alle jetzt neu gefundenen verbundenen Felder
    anzahl_verbundene = 1 + len(verbundene_felder)

    # Wir finden heraus wie viele weisse Felder es insgesamt in Quadratien gibt
    anzahl_weisse = 0
    for objekt in objektliste:
        if objekt.farbe == "w":
            anzahl_weisse += 1

    # So lange wir noch neue verbundene Felder finden
    while len(verbundene_felder) != 0:

        # Liste der Felder, die widerum an die eben schon gefundenen angrenzen
        neu_gefundene = []

        # Fuer jedes der eben gefundenen Felder wird widerum eine Untersuchung auf unbekannte, weisse
        # Nachbarfelder durchgeführt
        for feld in verbundene_felder:
            aktuelles_feld = feld
            neu_gefundene += suche_verbindungen(objektliste, aktuelles_feld)

        anzahl_verbundene += len(neu_gefundene)  # Anzahl der insgesamt verbundenen weissen Felder wird
        # entsprechend erhoeht
        verbundene_felder = neu_gefundene  # Die neu gefundenen werden wieder zu den verbundenen feldern
        # und die Suche kann weitergehen

    print("Es gibt " + str(anzahl_weisse) + " weisse Felder, davon sind " + str(
        anzahl_verbundene) + " miteinander verbunden!")

    if anzahl_weisse == anzahl_verbundene:
        print("Somit sind alle weissen Felder fuer Kassi erreichbar!")
    else:
        print("Kassi kann nicht alle weissen Felder erreichen :-(")

        # besuchte felder werden zu stein - jedes mal neu erreichbarkeit aller felder pruefen!


def kassi_bewedi(objektliste, kassi_anfang, kassi_ende):



    kopierte_objektliste = copy.deepcopy(objektliste)

    for index, item in enumerate(kopierte_objektliste):
        if item.objektkoordinaten == kassi_anfang.objektkoordinaten:
            kopierte_objektliste[index].kassi_steht = 0
            kopierte_objektliste[index].farbe = "s"
            kopierte_objektliste[index].schon_besucht = 1
        if item.objektkoordinaten == kassi_ende.objektkoordinaten:
            kopierte_objektliste[index].kassi_steht = 1
            kopierte_objektliste[index].farbe = "s"
            kopierte_objektliste[index].schon_besucht = 1

    return kopierte_objektliste


def kassi_finde_weg(objektliste):
    stammbaum = {}
    loesungen = []
    anzahl_weisse = 0
    for objekt in objektliste:
        if objekt.farbe == "w":
            anzahl_weisse += 1

    zustaende = [copy.deepcopy(objektliste)]

    for index, zustand in enumerate(zustaende):

        for i, item in enumerate(zustand):
            zustand[i].verbunden = 0

        kassi_ausgangspunkt = finde_kassi(zustand)
        reisemoeglichkeiten = suche_verbindungen(zustand, kassi_ausgangspunkt)

        for moeglichkeit in reisemoeglichkeiten:
            zustand = kassi_bewedi(zustand, kassi_ausgangspunkt, moeglichkeit)
            zustaende.append(zustand)
            stammbaum[index] = len(zustaende)-1
            print("Vaterzustand " + str(index) + " zeugte Zustand " + str(len(zustaende)-1))

            schon_besuchte = 0
            for feld in zustand:
                if feld.schon_besucht == 1:
                    schon_besuchte += 1
            if schon_besuchte == anzahl_weisse:
                loesungen.append(index)
                print(str(index) + "loest das Problem")
                from time import sleep
                sleep(1)
    print(stammbaum)

    return loesungen, stammbaum











