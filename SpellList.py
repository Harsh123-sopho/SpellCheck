# A trial small scale version of the custom dictionary class
Class myDictionary(object):
    def __init__(self):
        self.name= input('Enter the name of the dictionary file: ')
        if not ".dict" in self.name:
            self.name += '.dict'
        self.dictionaryList=[]

    def openDictionary(self):
        self.fRead=open(self.name,'r')
        for i in self.fRead:
            self.dictionaryList.append(i.strip())

    def addAWord(self,word):
        self.dictionaryList.append(word)
        self.dictionaryList.sort()

    def IsWordInDictionary(self,word):
        return word in self.dictionaryList

    def closeDictionary(self):
        self.fRead.close()
