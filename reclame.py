
from algemen_functies import mijn_functie_1, mijn_functie_2  


def aabieding_1( smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    nieuwe_prijs = round(nieuwe_prijs, 2)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak{smaak}, van {prijs} euro voor {nieuwe_prijs} euro"

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = round (totaal * btw, 2)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden"

def hoog_en_laag(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    gemiddelde_waarde = sum(mijn_lijst) / len(mijn_lijst)
    gemiddelde_waarde = round(gemiddelde_waarde, 2)
    return f"De inkomsten deze week zijn {gemiddelde_waarde} euro."

def meervoudig(invoer_lijst):
    korte_lijst = hoog_en_laag (invoer_lijst)
    return korte_lijst

def combinatie (mijn_lijst):
    resultaat = []
    for i in range (0, len(mijn_lijst)- 1, 2):
        a = mijn_lijst[i]
        b = mijn_lijst[i+1]
        resultaat = mijn_functie_2 (a, b)
        resultaat.append(resultaat)
    return resultaat

print (aabieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 343], 0.09))
print(hoog_en_laag([220, 430, 125, 160, 205, 90, 345]))
print (gemiddelde([220, 430, 125, 160, 205, 90, 345]))
print (meervoudig([10, 5, 3, 2, 1, 2, 9]))
print (combinatie([10, 5, 2, 2, 9, 1]))