"""
Python ist eine mächtige Programmiersprache. Um diese Mächtigkeit zu bändigen ist es
unabdingbar die grundlegenden Befehle zu beherrschen. Zu diesen zählen unter Anderem
die Befehle:
help, print, input, eval, format, type, id, abs, min, max, sum, range, len

    (a) Machen Sie sich mit den genannten Befehlen vertraut und beschreiben Sie
        stichpunktartig, was diese Build-Ins bewirken.
"""


"""
help:
    Dieser Befehl öffnet das help-Interface. In diesem kann man dann weitere Befehle
    eingeben, um detailierte Hilfestellungen zu bekommen.
"""
# help()

"""
print:
    Die Funktion print() stellt die ihn übergebenen Parameter im Terminal dar. 
    '\n' -> Blank line
    ''   -> Empty line   
"""
# print("Hello! \nHow are you?")

"""
input:
    Die Methode input() ließt die Benutzereingabe ein und gibt diesen als String 
    wieder.
"""
# input("Write something: ")

"""
eval:
    Die eval() Methode analysiert den an diese Methode übergebenen Ausdruck und 
    führt den Code innerhalb des Programms aus.
"""
# x = 1
# print(eval('x + 1'))

"""
format:
    Diese Methode formatiert einen angegeben Wert und fügt diesen in einen Platz-
    halter ein. Der Platzhalter wird durch {} repräsentiert.
"""
# for i in range(1, 11):
#     print("There are {} boxes!".format(i))

"""
type:
    Die type()-Funktion gibt entweder den Typ des Objekts oder einen neues Typ-
    objekt basierend auf den übergebenen Argumenten zurück.
"""
# numbers_list = [1, 2]
# print(type(numbers_list))

"""
id:
    Die id()-Funktion gibt die Identität (eindeutige Ganzzahl) eines Objekts zurück.
"""
# print(id(5))

"""
abs:
    Diese Methode gibt den absoluten Wert der angegebenen Zahl zurück.
"""
# a = -20
# print(abs(a))

"""
min:
    min() gibt das kleinste Element in einer Liste zurück.
"""
# numbers = [1, 2, 3, 4, 5, 6]
# smallest_number = min(numbers)
# print(smallest_number)

"""
max:
    max() gibt das größte Element einer Liste wieder.
"""
# numbers = [1, 2, 3, 4, 5, 6]
# largest_number = max(numbers)
# print(largest_number)

"""
sum:
    Die sum()-Funktion addiert alle Elemente einer Liste zusammen.
"""
# numbers = [1, 2, 3, 4, 5, 6]
# sum_number = sum(numbers)
# print(sum_number)

"""
range:
    Die range()-Funktion gibt eine unveränderliche Folge von Zahlen zwischen der
    angegbenen Start-Zahl und der End-Zahl zurück. WICHTIG: range() hört einen
    Wert vor dem End-Wert auf.
"""
# print(list(range(1, 10)))

"""
len:
    Die len()-Funktion gibt die Anzahl der Elemente (Länge) in einem Objekt zurück
"""
# numbers = range(1, 10)
# print("Length of", numbers, "is", len(numbers))