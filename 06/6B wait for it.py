with open("06/input.txt") as fil:
    tid = int(fil.readline().split(":")[1].replace(" ","").strip())
    rekord = int(fil.readline().split(":")[1].replace(" ","").strip())
    bytte=False
    i=0
    while bytte==False:
        if i*(tid-i) > rekord:
            bytte=i
        i +=1
    print("Bytter ved: ", bytte, "løsning: ", tid-2*(bytte-1)-1)
    #hva vi greier er normalfordelt og kan speiles om midten av løsningsområdet. Så om vi vet når vi begynner å få til rekorden, vet vi alt vi trenger:
    