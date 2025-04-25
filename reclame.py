
from algemen_functies import mijn_functie_2 

def combinatie (invoer_lijst_2):
    kort_lijst = hoog_en_laag (invoer_lijst_2)
    return mijn_functie_2 (kort_lijst)

def aabieding_1( smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    nieuwe_prijs = round(nieuwe_prijs, 2)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak{smaak}, van {prijs} euro voor {nieuwe_prijs} euro"

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    totaal_met_btw = round (totaal_met_btw, 2)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden"

def hoog_en_laag(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def meervoudig(invoer_lijst):
    hoogste_en_laagste = hoog_en_laag (invoer_lijst)
    laatste_waarde = invoer_lijst[-1]
    return[hoogste_en_laagste[0], laatste_waarde]

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde = totaal / aantal
    gemiddelde_waarde = round(gemiddelde_waarde, 2)
    gemiddelde_str = str(gemiddelde_waarde).replace('.', ',')
    return f"De inkomsten deze week zijn {gemiddelde_str} euro"

print (gemiddelde([220, 430, 125, 160, 205, 90, 345]))
print (meervoudig([10, 5, 3, 2, 1, 2, 9]))