"""
    (a) Schreiben Sie ein Python-Script, das den Benutzer nach seinem Namen fragt
        und diesen in die Variable Name schreibt.
    (b) Erweitern Sie ihr Programm aus Aufgabenteil (a) so, dass der Benutzer nach
        seinem Namen, Alter und seiner Matirkelnummer gefragt wird, und das Programm
        dies in einem Satz ausgibt
    (c) Schreiben Sie das Programm so um, dass es das Geburtsjahr ausrechnet und
        dieses mit ausgibt.
"""

# (a)
name = input("Type your name: ")

# (b)
age = int(input("Type your age: "))
matnr = input("Type your Matirkelnumber: ")
print(name, "is", age, "years old and has the Matrikelnumber", matnr)

# (c)
day_of_birth = input("Enter your day of birth (YYYY-MM-DD): ")
year = ""
month = ""
day = ""
for i in range(0, 4):
    year += day_of_birth[i]
print(year)
from datetime import datetime
datetimeObj = datetime.now()
print(datetimeObj)