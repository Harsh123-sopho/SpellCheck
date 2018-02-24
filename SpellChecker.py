from SpellList  import *
from Scanner import *

#This file has the necessary code for spell check

if __name__=='__main__':
    print('Welcome to the document spell checker!\nMake sure that your document and the personal dictionary, or the default one we have provided are in the same directory as this code.')
    dictionary = myDictionary()
    print('What do you plan to do: ')
    print('1. Add a new word to your dictionary')
    print('2. Scan a document for errors')
    n = input('Enter the task number for execution: ')

    if n == '1':
        dictionary.openDictionary()
        word=input('What word would you like to add? ')
        if dictionary.isWordInDictionary(word):
            print('Word already exists!')
        else:
            dictionary.addAWord(word)
            dictionary.saveChanges()
            print('Word successfully added to dictionary!')
        dictionary.closeDictionary()

    elif n == '2':
        print('yet to be implemented')

    else:
        print('Not an option')
    
    



