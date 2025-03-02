def presenteer(dictionary, totaal):
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")
    print("=" * 20)
    print(f"totaal : {totaal} euro")

mijn_dict = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750,
} 

totaal = 5220

presenteer(mijn_dict, totaal)