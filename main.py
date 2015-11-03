import datenstruktur
import algorithmus
import fenster
import threading
import time

datenstruktur.still = 1

dateiname = fenster.erstelle_fragefenster()
# Datein einlesen & verarbeiten
inhalt_datei = datenstruktur.einlesen_datei(dateiname)
liste_der_felder = datenstruktur.verarbeiten_datei(inhalt_datei)


def algorithmus_funktion():
    # Algorithmen zur Loesung der Aufgabenstellungen
    time.sleep(0.5)
    algorithmus.verbindungstest(1, liste_der_felder)
    algorithmus.kassi_finde_weg(liste_der_felder)


algorithmen_task = threading.Thread(target=algorithmus_funktion)
algorithmen_task.start()
fenster.erstelle_fenster(liste_der_felder)
