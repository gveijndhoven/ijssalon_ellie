import csv
from helper import *
from presentatie import *

boekhoud_dictionary = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750,
}    

totaal_inkomsten = boekhoud_dictionary.values()

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in boekhoud_dictionary.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])