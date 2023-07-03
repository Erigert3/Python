import json
from difflib import get_close_matches
f=open("data.json")
data=json.load(f)

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        decide=input("press y for yes or n for no")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            return("this word doesn't even exist")
        else:
            return("press y or n.")

    else:
        print("this word doesn't exist")

word=input("enter the word you want to search")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
