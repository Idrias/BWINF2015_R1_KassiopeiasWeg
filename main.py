"""
Aufgabenteil 1:
Kassiopeia (K) moechte jedes helle Feld (W) besuchen. Schwaze Felder (S) duerfen nicht betreten werden.
Entscheidend ist nicht die schnellste Moeglichkeit, die Felder abzuarbeiten, sondern ob es ueberhaupt moeglich ist,
alle zu besuchen.

Wann ist es nicht moeglich?
Wenn zwei verschiedene helle Zonen durch eine schwaze Barriere getrennt werden.

Wie erkennt man das?
Haengen alle hellen Flaechen zusammen?]
"""

import datenstruktur

mein_feld = datenstruktur.Feld("schwarz", 42, 43, 1)
a = datenstruktur.einlesen_datei("kassiopeia0.txt")
datenstruktur.verarbeiten_datei(a)

