prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5 
} 
aanbieding = prijzen["vanille"], * 0.8
reclame_tekst = f"vandaag in de aanbieding: vanille_ijs, 1 liter - slechts {aanbieding}"

reclame_tekst2 = reclame_tekst [: 36]

reclame_tekst3 = reclame_tekst2.upper() 

reclame_tekst4 = reclame_tekst3.replace("", "\n")

for e1 in reclame_tekst4.split("\n"):
    e1 = e1.lower()

    if len (e1) > 4:
        print(e1)
woorden_lijst = reclame_tekst4.split("/n")
lange_woord = [woord.lower() for woord in woorden_lijst if len(woord)> 4]

if len(lange_woord) == len([w for w in woorden_lijst if len(w) > 4]):
    print ("Controle is gelukt.")
    print("bestand tijdelijke.py\ngecodeerd")
 

