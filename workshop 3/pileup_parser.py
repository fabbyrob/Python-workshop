def Parser(aFile):
        for line in open(aFile, 'r'):
            yield Record(line)
            
class Record:
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
        return "Record("+str(self.CHROM)+", "+str(self.BASE)+")"
        
myFile = "pile.txt"

for record in Parser(myFile):
    print(record)
        
#How many SNPS are there with QUAL > 30?
#how many bases are there on each chromosome with REF = "A"
#how many sites are there on each chromosme with QUAL > 40
#How many sites are there on each chromosome?
#what is the mean depth of each chromosme?
#Make a histogram of qualities in this file. 
        