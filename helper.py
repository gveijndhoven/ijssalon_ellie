from boekhouding import *

def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    
def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return (f"Het bedrag per persoon is {bedrag_pp} Euro")

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append("=" * len(tekst))
    return uit

def som():
    return sum(totaal_inkomsten.values())