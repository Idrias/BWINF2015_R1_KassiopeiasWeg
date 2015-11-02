import datenstruktur
import algoritmus

datenstruktur.still = 1

inhalt_datei = datenstruktur.einlesen_datei("kassiopeia5.txt")
liste_der_felder = datenstruktur.verarbeiten_datei(inhalt_datei)
algoritmus.verbindungstest(liste_der_felder)
algoritmus.kassi_finde_weg(liste_der_felder)
