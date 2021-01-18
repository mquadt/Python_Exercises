"""
Die Formel zur Umrechnung von Fahrenheit in Celsius lautet:
celsius = 5/9 * (fahrenheit - 32.0)
    (a) Schreiben Sie ein Programm, das eine Angabe von Celsius in Fahrenheit
        umrechnet.
    (b) Schreiben Sie ein Programm, das eine Angabe von Fahrenheit in Celsius
        umrechnet
"""

# (a)
def fahrenheitZuCelsius():
    print("Celsius: " + str((5/9)*(float(input("Information degree Fahrenheit: "))-32.0)))

fahrenheitZuCelsius()

# (b)
def celsiusZuFahrenheit():
    print("Degree Fahrenheit: " + str((float(input("Information Celsius "))*1.8)+32))

celsiusZuFahrenheit()