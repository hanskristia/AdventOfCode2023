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
    seeds =  [int(x) for x in  fil.readline().split(":")[1].strip().split(" ")]
    
    maping = []
    for linje in fil:
        if ":" in linje:
            print(linje,end=" ")
        elif "\n" == linje:
            if maping:
                seeds=AtBmap(seeds,maping)
                print(seeds)
                maping=[]
        else:
            maping.append( [int(x) for x in linje.strip().split(" ")])
    seeds=AtBmap(seeds,maping)
    print(seeds)
    print("løsning: ",min(seeds))        
    
    
    
