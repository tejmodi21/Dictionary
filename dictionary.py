import json
import difflib
from difflib import get_close_matches

data =json.load(open("/Users/tejmodi/PycharmProjects/demo/data.json", encoding = "utf-8-sig"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        a=get_close_matches(word,data.keys(),cutoff=0.8)
        if not a:
            return "Please enter the correct word as the word doesn't exists "
        else:
            yes_no=input("Did you mean %s word ?Enter Y if Yes and N if NO" %a[0])
            if yes_no=="Y":
                return data[a[0]]
            elif yes_no=="N":
                return "The word was incorrect. Please double check the word."
            else:
                return "We didn't understand your entry."
    else:
        return "Please enter the correct word as the word doesn't exists"

word = input("Enter the word:")

#output = translate(word)

if type(output) == list:
    count = 1
    for item in output:
        print ("%s) %s" %(i,item))
        count += count
else:
    print(translate(word))
