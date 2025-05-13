import csv
from helper import som
from presentatie import *

inkomsten ={ 
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

totaal_inkomsten = som(inkomsten)
presenteer( inkomsten, totaal_inkomsten)

# emporteer naar CSV-bestand
with open ("boekhouding.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for key, value in inkomsten.items():
        writer.writerow([key, value])