
løsning=0
with open("02/input.txt") as fil:
    for linje in fil:
        kuler = {
            "red":0,
            "green":0,
            "blue":0  
        }
        godkjent=True
        id,rest = linje.split(":")
        id=int(id[5:]) # Spill ID
        runder = rest.split(";") #' 3 blue, 4 red'
        # print(id,runder)
        
        for trekk in runder:
            farger = trekk.split(",")   #3 blue
            for type in farger:
                # print(type)
                tall,farge=type.strip().split(" ")
                tall=int(tall)
                if tall > kuler[farge]:
                    kuler[farge]=tall
        produkt = 1
        for i in kuler.values():
            produkt *= i
        løsning +=produkt
    print(løsning)
