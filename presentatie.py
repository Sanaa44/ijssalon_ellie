def presenteer(inkomsten, totaal):
    for product, bedrag in inkomsten.items():
        print("f{product}: {bedrag} euro")
    print("=" * 10)
    print(f" Totaal: {totaal} euro")