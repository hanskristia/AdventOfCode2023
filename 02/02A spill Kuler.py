Kuler = {
    "red":12,
    "green":13,
    "blue":14  
}
løsning=0
with open("02/input.txt") as fil:
    itt=0   #For å sjekke antall itterasjoner, kun for å sjekke optimaliseringer
    for linje in fil:
        godkjent=True
        id,rest = linje.split(":")
        id=int(id[5:]) # Spill ID
        hånd = rest.split(";") #' 3 blue, 4 red'
        # print(id,runder)
        
        for kulene in hånd:
            for kule in kulene.split(","): #3 blue
                # print(type)
                antall,farge=kule.strip().split(" ") #Strip fjerner overflødige mellomrom.
                antall=int(antall)
                itt+=1
                if antall > Kuler[farge]:
                    godkjent=False
                    break   # ~50 mindre itt, hopper ut av kulene
            if not godkjent: break #~ 300 mindre itt, hopper ut av runden.
            
        if godkjent:
            løsning+=id
    print(løsning,itt)
