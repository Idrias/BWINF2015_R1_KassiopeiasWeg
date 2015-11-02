import datenstruktur
import algoritmus
import fenster

datenstruktur.still = 1

# Datein einlesen & verarbeiten
inhalt_datei = datenstruktur.einlesen_datei("kassiopeia0.txt")
liste_der_felder = datenstruktur.verarbeiten_datei(inhalt_datei)
#fenster.build_window(liste_der_felder)


# Algoritmen zur Loesung der Aufgabenstellungen
algoritmus.verbindungstest(liste_der_felder)
algoritmus.kassi_finde_weg(liste_der_felder)
