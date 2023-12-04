
with open("04/input.txt") as fil:
    løsning=0
    for linje in fil:
        tall= [i.strip().split(" ") for i in linje.split(":")[1].split("|")]
        potens=-1
        for i in tall:
            while "" in i:
                i.remove("")
       
        for i in tall[1]:
            
            if i in tall[0]:
                potens+=1
        if potens != -1:
            verdi=pow(2,potens)
        else :
            verdi = 0
        # print(verdi, tall[0],tall[1] )
        løsning+= verdi

    print(løsning)

# 102370 To high