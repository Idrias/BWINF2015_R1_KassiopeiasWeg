import datenstruktur
import algoritmus
import fenster
from time import sleep
from threading import *

datenstruktur.still = 0

def abc():
    algoritmus.verbindungstest(liste_der_felder)
    sleep(1)


inhalt_datei = datenstruktur.einlesen_datei("kassiopeia7.txt")
liste_der_felder = datenstruktur.verarbeiten_datei(inhalt_datei)

a = Thread(target = abc)
a.start()


fenster.build_window(liste_der_felder)






