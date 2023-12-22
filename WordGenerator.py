import json
import random
print("Welcome to the 2023 sentence generator!")

datafile = open("Words.json")
data = json.load(datafile)
string = ""

wordcount = 0

for i in data["Words"]:
    wordcount+=1

print(f"{wordcount} Words detected in json file.")
words = int(input("How many words would you like? \r\n"))
for i in range(words):
    random_word = random.choice(data["Words"])
    
    if i == 0:
        string = random_word
    else:
        string+=" "+random_word.lower()
print(string)
datafile.close
input("Enter to exit...")
