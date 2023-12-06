
with open("06/test.txt") as fil:
    tid = fil.readline().split(":")[1].strip().split(" ")
    distanser = fil.readline().split(":")[1].strip().split(" ")
    while "" in tid:
        tid.remove("")
    while "" in distanser:
        distanser.remove("")
    print(tid,distanser)
    løsning=1
    for tid,rekord in zip(tid,distanser):
        tid,rekord=int(tid),int(rekord)
        seiere=0    
        for i in range(tid):
            if i*(tid-i) > rekord:
                seiere+=1
        løsning*= seiere
    print(løsning)