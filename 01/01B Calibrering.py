#Feil svar, endrer strategi, må løse twone -> 2 1.
verdier=["0","1","2","3","4","5","6","7","8","9","zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as fil:
    løsning=0
    
    for linje in fil:
        mins,maks=len(linje),0
        
        for tall in verdier:
            if tall in linje:
                a,b = linje.find(tall),linje.rfind(tall)
                if a < mins and a != -1:
                    mins=a
                    start=tall
                if b > maks and b!=-1:
                    maks=b
                    slutt=tall
        a = verdier.index(start) % 10
        b = verdier.index(slutt) % 10
        tall =int(str(a)+str(b)) 
        løsning+=tall
        print("neste:")
        print(linje,start,slutt,a,b,tall,løsning)
        
        
    print(løsning)
            
    