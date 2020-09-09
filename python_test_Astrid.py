## Basic python test 

#%%
# Task 1: Adding machine
1+1
def addfunction(x,y):
    return x + y 

addfunction(-1,8)
# returns 7
# WORKS

#%%
# Task 2: Character count
def countingcharacters(s, i):
    # converts string + letter to lowercase 
    lower_s = s.lower()
    lower_i = i.lower()
    # checks if letter is in string
    if lower_i in lower_s:
        count = lower_s.count(lower_i) # use .index if I want position of first occurrence
        return count
    else:
        print("The letter does not occur in the given word")
countingcharacters("INTERDISCIPLINARY", "n")
# returns 2
# WORKS 
# %%
# Task 3: Function isEven
# 1) test if a given number is even or odd, 
# return True for even, False for odd 
# (only integers)
# 2) given a list (or array) of numbers, use the above function to determine the number of even items in the list

# check if a single number is even
def isEven(number):
    if number %2 == 0: # bc there are no "leftover" integers when diving an equal number by 2
        return True
    else:
        return False
isEven(90)

# Answer how many numbers of a list that are even (instead of odd)
def CountEvenItems(numberlist):
    EvenNumbersList = []
    for number in numberlist:
        if isEven(number) == True:
            EvenNumbersList.append(1)
        elif isEven(number) == False:
            EvenNumbersList.append(0)
    if sum(EvenNumbersList) > 0:
        print("%d out of %d numbers in the list are even" % (sum(EvenNumbersList),len(numberlist)))
    else: 
        print("There are no even numbers in the list")

# Test it
numberlist = [10,45,0,-4,99,43,2]
CountEvenItems(numberlist)
# OR
CountEvenItems(numberlist=[10,45,0,-4,99,43,2])
# Returns 4 out of 7 numbers in the list are even
# WORKS

#%%
# Task 4: Search in list
# Give the largest value out of a list of floating-point numbers
def LargestValueItem(floatnumberlist):
    Largestvaluelist = []
    for number in floatnumberlist:
        currentnumber = number
        if currentnumber >= sum(Largestvaluelist):
            Largestvaluelist.append(currentnumber)

#%% 
# Task 5: String and loops 
def RemoveCharctersFunc(word):
    length = len(word)
    print(word)
    print()

#%%
# Task 6: Get dict keys 
def GetDictKeys(dictionary):

#%%
