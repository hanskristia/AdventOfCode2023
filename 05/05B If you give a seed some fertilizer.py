# Uferdig, N blir for stor, må avgrense søket.
# Må se på områder, og ikke spesifikke tall. Kan sees som et  slicing problem? starter med ulike staver med ulike lengder,enten så deles staven opp, eller så går den videre.
inputs=[]
def AtBmap(seeds:list,map:list)->list:
    newSeeds=[]
    for seed in seeds:
        funnet=False
        for i in range(len(map)):
            destination,source,length = map[i]
            # print(destination,source,length)
            if source <= seed and seed <= source + length:
                # print(seed,"funnet, ny:",seed+(destination-source) )
                newSeeds.append(seed+(destination-source))
                funnet=True
                break

        if not funnet:
            # print("ikke funnet")
            newSeeds.append(seed)
    return newSeeds

with open("05/input.txt") as fil:
    # En brute force metode:
    seeds=[]
    linje=[int(x) for x in fil.readline().split(":")[1].strip().split(" ")]
    # print(linje)
    for i in range(0,len(linje),2):
        # print(i,i+1)
        for j in range(linje[i],linje[i]+linje[i+1]):
            # print(j,end="")
            seeds.append(j)
    # men fra input: 41218238 421491713
    # Så N er minimum 10^8, dette blir for stort Må redusere problemet
    # print(seeds)
    maping = []
    for linje in fil:
        if ":" in linje:
            # print(linje,end=" ")
            pass
        elif "\n" == linje:
            if maping:
                seeds=AtBmap(seeds,maping)
                # print(seeds)
                maping=[]
        else:
            maping.append( [int(x) for x in linje.strip().split(" ")])
    seeds=AtBmap(seeds,maping)
    # print(seeds)
    print("løsning: ",min(seeds))        
    
    
    
