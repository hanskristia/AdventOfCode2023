
def sjekkTall(i,start,bredde):
    løsning=0
    slutt=start+bredde
    tall=oversikt[i][start:slutt]
    debugStr="-> "+tall+"\n"

    #Må sjekke over, ved sidene og nedover, samt diagonalt.
    sjekkStreng = ""
    
    for h in range (max(0,i-1),min(høyde,i+2)):
        debugStr+=f"h:{h+1} \t"
        #går igjennom høyden
        for b in range (max(0,start-1),min(lengde,slutt+1)):
            debugStr+=oversikt[h][b]
            sjekkStreng += oversikt[h][b]
        debugStr+="\n"
    # print(sjekkStreng)
    sjekkStreng=sjekkStreng.replace(".","")
    sjekkStreng=sjekkStreng.replace(tall,"")
    
    if(sjekkStreng):
        løsning=int(tall)
        # print("legger til: \n",debugStr)

    # else:    print("legger ikke til: \n",debugStr)
    return løsning
    

with open("03/input.txt") as fil:
    #lager en matrise for deloversikten
    oversikt=[]
    for linje in fil:
        oversikt.append(linje.removesuffix("\n")) 
            #Fjerner siste \n.
    # for linje in oversikt:
    #     print(linje)
    lengde=len(oversikt[0])
    høyde=len(oversikt)
    løsning=0
    for i in range(høyde):
        start,bredde =-1,0
        for j in range(lengde):
            if oversikt[i][j].isdigit():
                if start == -1 :
                    start=j
                bredde += 1
                if(j==lengde-1):
                    løsning+=sjekkTall(i,start,bredde)
                    #tilbakestiller
                    start=-1
                    bredde=0
                    tall=0
                    debugStr=""
            elif start !=-1:
                løsning+=sjekkTall(i,start,bredde)
                #tilbakestiller
                start=-1
                bredde=0
                tall=0
                debugStr=""
            # print (oversikt[i][j],start,bredde)
        
    print(løsning)


    
