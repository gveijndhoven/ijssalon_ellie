from statistics import mean
from algemene_functies import mijn_functie_2

# aankondigingsregel
print("Gegevens van de ijssalon")
print()

def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs:.2f} euro."

# eerste printregel; de reclame
print(aanbieding_1("aardbei", 4, 0.1))
print()


def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
resultaat = inkomsten_totaal(inkomsten, btw)

# tweede printregel; het resultaat
print(resultaat)
print()

def laag_en_hoog(mijn_lijst):
    return f"Laagste dagopbrensgt {min(mijn_lijst)} euro, hoogste dagopbrengst {max(mijn_lijst)} euro."

# derde printregel; laagste en hoogste bedrag
print(laag_en_hoog(inkomsten))
print()

def gemiddelde(mijn_lijst):
    return f"De gemiddelde inkomsten deze week zijn {mean(mijn_lijst)} euro."

# vierde printregel; gemiddelde
print(gemiddelde(inkomsten))
print()

def hoog_en_laag(invoer_lijst):
    hoogste = max(invoer_lijst)
    laagste = min(invoer_lijst)
    return [hoogste, laagste]

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

getallenlijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(getallenlijst)
# vijfde printregel; hoogste en laagste
print("Hoogste en laagste getal uit de getallenlijst:", resultaat)
print()

def combinatie(invoer_lijst_2):
    korte_lijst = hoog_en_laag(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

resultaat_combinatie = combinatie(getallenlijst)
# zesde printregel; combinatie
print("Uitkomst combinatie functie:", resultaat_combinatie)
    
    