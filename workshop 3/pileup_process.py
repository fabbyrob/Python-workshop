myPileup = open("pile.txt","r")

for line in myPileup:
    line = line.split()
    CHROM = line[0]
    BASE = int(line[1])
    REF = line[2]
    ALT = line[3]
    QUAL = int(line[4])
    SNPQUAL = int(line[5])
    MAPQUAL = int(line[6])
    DEPTH = int(line[7])
    READS = line[8]
    READQUALS = line[9:]
    print(CHROM+" "+str(BASE))
