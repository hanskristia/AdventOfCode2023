#Feil svar, usikker på hvorfor, men endrer strategi.
verdier=["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("01/input.txt") as fil:
    nyTekst=""
    for linje in fil:
    # En runde med preprosessering: 
        # print("\n",linje)
        for i in range(10):
            linje=linje.replace(verdier[i],verdier[i][0]+str(i)+verdier[i][-1])
            #Bytter tekst til tall, og legger til første og siste bokstav.s
        nyTekst+=linje
        # print(linje)

    løsning = 0
    # open("01/preprosess.txt","w").write(nyTekst) # For å se på løsningen

    for linje in nyTekst.splitlines():
        #Samme som i 1A.
        start,slutt=0,0
        for i in linje:
            if i.isdigit():
                start=i
                break
        for i in reversed(linje):
            if i.isdigit():
                slutt=i
                break
        tall =int(start+slutt) 
        # print(linje,start,slutt,tall)
        løsning+=tall
    print(løsning)