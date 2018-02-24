import string

class docScan():
    def __init__(self):
        self.word_list=[]

    def scan(self,file):
        fread = open(file,'r')
        for k in fread:
            for j in [i.strip(string.punctuation) for i in k.split()]:
                self.word_list.append(j)
        fread.close()

#class tester code
if __name__=="__main__":
    g=docScan()
    g.scan("testDoc.txt")
    for i in g.word_list:
        print(i)
