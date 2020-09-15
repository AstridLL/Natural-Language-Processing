# operations we want to achieve:
# turn text into bigrams 
# add padding around sentences to avoid words 
# that are next to each other but not in the same sentence
import re
with open("peter.txt") as f:
    counts = {}
    for line in f:
        for word in line.split():
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

for word in counts:
    print(word, counts[word])

def GetUnigram(text, targetunigram):
    if text.endswith(".txt"):
        open(txt) as f:
            counts = {}
            
    str.endswith(suffix[, start[, end]])
