def mijn_functie_1(x):
    return x * x

print (mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))

def mijn_functie_2(lijst):
    getal1 = lijst[0]
    getal2 = lijst[1]
    return [getal1 + getal2, getal1 - getal2, getal2, getal1 / getal2]
