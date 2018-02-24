# A trial small scale version of the custom dictionary class
class myDictionary(object):
    def __init__(self):
        self.name= input('Enter the name of the dictionary file: ')
        if not ".dict" in self.name:
            self.name += '.dict'
        self.dictionaryList=[]
        self.fAppend=open(self.name,'a')
        self.fAppend.close()

    def openDictionary(self):
        self.fRead=open(self.name,'r')
        for i in self.fRead:
            i = i.lower()
            self.dictionaryList.append(i.strip())

    def addAWord(self,word):
        self.dictionaryList.append(word.lower())
        self.dictionaryList.sort()

    def isWordInDictionary(self,word):
        return word.lower() in self.dictionaryList
    
    def saveChanges(self):
        self.fWrite=open(self.name,'w')
        for i in self.dictionaryList:
            self.fWrite.write(i+"\n")
        self.fWrite.close()
        
    def closeDictionary(self):
        self.fRead.close()
