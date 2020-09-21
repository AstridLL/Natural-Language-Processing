astring = "Hello world!"
print(astring[3:8:2]) #(start:stop:step)
#%%
1+1
#%%
#%%

print("hello")

string = "hello there"
print(string)

import nltk
#import tensorflow as tf

# lidt ekstra code 
# lidt flere 
# ændring

#import stanza

#stanza.download("da")

#stanza.download("en")

# %%
names = ["Pia", "Ina", "Rebecca", "Lotte", "Ida", "Michelle"]
jobs = ["stewardess", "cleaner", "consultant", "gamer", "athlete", "post"]
hours = [24,37,45]
#import random

def namefunction(name):
    if name in names:
        namesnumber = names.index(name)
        jobsnumber = jobs[namesnumber]
        #return jobsnumber

        if jobsnumber in jobs:
            yourhours = random.choice(hours)
            #return yourhours
            print("So your name is %s, your job is %s, and you work %d hours a week." % (name, jobsnumber, yourhours))
        else:
            print("there is an error")
    else:
        print("The name you wrote did not match with any of the names in the nameslist")

namefunction("Lotte")

# loop through the entire list of names 
for name in names:
    namefunction(name)

# %%

def mineditdist(source, target):
    n = len(source)
    m = len(target)
    
    for row i from one to n:
        
# %%






# %%
print("hello world")
# %%
# variables
character_name = "John"
character_age = "35"
character_age = 50.87
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + ".")

# Bolean values 
ismale = False

# string values 
phrase = "Girraffe academy"
print(phrase + " is cool")
print(phrase.upper())
print(phrase.lower())
phrase.isupper() # returns true/false 
phrase.upper().isupper() # returns true bc it turns it into upper first

len(phrase)
#indexing 
phrase[2]
print(phrase.index("raf")) # gives number of where it starts when there are multiple characters
print(phrase.replace("LOL", "Elephant"))
phrase.replace("Elephant","Giraffe")

# %%
