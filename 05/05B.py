# Uferdig, N blir for stor, må avgrense søket.
# Må se på områder, og ikke spesifikke tall. Kan sees som et  slicing problem? starter med ulike staver med ulike lengder,enten så deles staven opp, eller så går den videre.
inputs=[]
def AtBmap(seeds:list,map:list)->list:
    newSeeds=[]
    seeds.sort()
    # print(seeds)
    for seed in seeds:
        # print(seed)
        start,område = seed
        
        for i in range(len(map)):
            destination,source,length = map[i]
            # print(destination,source,length)
            # print(f"start {start},\t område: {område}, ende: {start+område}\t d: {destination},\t s: {source},\t l: {length},\t b: {length+source}")
            if start >= source and start<= source+length:
                while start < source + length and område>0:
                    # om starten er innenfor dette området
                    # print(start+område, source+length)
                    ende = min(start+område, source+length)
                    # Da blir slutten minste del av start og source rods
                    nyområde=ende-start
                    
                    newSeeds.append([destination+(start-source),nyområde]) 
                    # print(f"Nytt frø: {newSeeds[-1]}, {sum(newSeeds[-1])}")
                    #legger til nytt frø
                    område=område-nyområde
                    start=ende
            elif(start <= source and source <= start+område):
                #om source er innenfor:
                #kan lage et nytt frø fra:
                #source til enden
                ende = min(start+område, source+length)
                nyLengde=ende-source
                newSeeds.append([destination,nyLengde])
                # print(f"Nytt frø: {newSeeds[-1]}, {sum(newSeeds[-1])},fra{source},{ende}")
                if (start+område > source + length):
                    #om vi deler staven i to deler:
                    #sketsj å legge til midt i, men funker det?
                    seeds.append([source+length, start+område-(source+length)])
                    print("Delte i to, legger til et nytt frø",seeds[-1])
                    område=source-start
                else:
                    område=område-nyLengde
            else:
                # print("ikke inni")
                pass
        if område>0:

            # Denne biten av frøet er ikke funnet:
            newSeeds.append([start,område]) 
            # print(f"Nytt frø: {newSeeds[-1]}, ender på: {sum(newSeeds[-1])}")
                    
    # print(newSeeds)
    return newSeeds

with open("05/input.txt") as fil:
    # En brute force metode:
    seeds=[]
    linje=[int(x) for x in fil.readline().split(":")[1].strip().split(" ")]
    for i in range(0,len(linje),2):
        seeds.append([linje[i],linje[i+1]])
        #0 er start, 1 er range for frøet   
            
    # men fra input: 41218238 421491713
    # Så N er minimum 10^8, dette blir for stort, Må redusere problemet
    print(seeds)
    maping = []
    for linje in fil:
        if ":" in linje:
            print(linje,end=" ")
            pass
        elif "\n" == linje:
            if maping:
                print(maping)
                seeds=AtBmap(seeds,maping)
                
                maping=[]
        else:
            maping.append( [int(x) for x in linje.strip().split(" ")])
    
    # seeds=AtBmap(seeds,maping)
    seeds.sort()
    print(seeds)
    print("løsning: ",min(seeds))        
    
    
    
# løsning:  [0, 3050020], 0 er ikke riktig
# løsning:  [0, 42496570], 0 er ikke riktig

# 69703574 er for lavt, noe feil i algoritmen
# Må kanskje skrives omm fra start igjen.