class Record():
    def __init__(self, data):
        data = data.split()
        self.CHROM = data[0]
        self.BASE = int(data[1])
        self.REF = data[2]
        self.ALT = data[3]
        self.QUAL = int(data[4])
        self.SNPQUAL = int(data[5])
        self.MAPQUAL = int(data[6])
        self.DEPTH = int(data[7])
        self.READS = data[8]
        self.READQUALS = data[9:]
        
    def __str__(self):
        return "Record("+self.CHROM+", "+str(self.BASE)+")"

myPileup = open("pile.txt", "r")

for line in myPileup:
    myRecord = Record(line)
    print(myRecord)