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
´
# %%
