#  AUTHOR:  Michael O'Brien
#  CREATED:  08 June 2018
#  UPDATED:  11 June 2018
#  DESCRIPTION:  Dictionary program that will return a definition for a word


#  Import the JSON module to read the dictionary of words and defnitions
import json


#  Import the difflib library to allow for string matching in case the user misspells a word
from difflib import get_close_matches


#  Load the JSON dictionary into the application
dictionary = json.load(open('data.json','r'))


def get_definition():
    while True:
        word = input('Please enter a word you want the defintion for or 99 to exit:  ')
        word = word.lower()
        if word == '99':
            print('Thank you for using my dictionary.  Have a great day.')
            break
        else:
            if word in dictionary:
                definitions = dictionary[word]
                for definition in definitions:
                    print (definition)
            elif len(get_close_matches(word, dictionary.keys())) > 0:
                print ('Did you mean %s instead?' %get_close_matches(word, dictionary.keys())[0])
                search = input ('Do you want the definition of this word?  Y/N:  ')
                if search.lower() == 'y':
                    newWordDef = dictionary[get_close_matches(word, dictionary.keys())[0]]
                    for definition in newWordDef:
                        print (definition)
                else:
                    print ("Word not found")
            else:
                print ('Word not found')


get_definition()
