#Hva trenger vi: 
# Kort nummer, en "heap-struktur, en teller for antall kort"
with open("04/input.txt") as fil:
    løsning=0
    kort = []
    # Henter ut scratchcards, legger de inn i kort listen:
    for linje in fil:
        tall= [i.strip().split(" ") for i in linje.split(":")[1].split("|")]
        for i in tall:
            while "" in i:
                i.remove("")
        kort.append([tall,1])
    
    for i in range(len(kort)):
        tall,kopier = kort[i]
        
        # Finner antall vinnere i denne rekken
        vinnere=0
        for j in tall[1]:
            if j in tall[0]:
                vinnere+=1
       
        
        # Legger til kort til senere rekker, avhengig av hvor mange kort vi har
        for j in range(i+1,i+vinnere+1):
            if j < len(kort):
                kort[j][1]+= kopier
    # finner sum av antall kort
    løsning=0
    for tall in kort:
        løsning+=tall[1]
        # print(tall[1])
    print(løsning)
