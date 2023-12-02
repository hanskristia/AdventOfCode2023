with open("01/input.txt") as fil:
    løsning=0
    for linje in fil:
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
        # print(start,slutt,tall)
        løsning+=tall
        exit
    print(løsning)
    