## Basic python test 

#%%
# Task 1: Adding machine
1+1
def addfunction(x,y):
    return x + y 

#%%
# Task 2: Character count
def countingcharacters(s, i):
    if i in s:
        count = s.index(i)
        return count

# %%
# Task 3: Function isEven
# test if a given number is an even number, return true/false
# given a list of numbers, use the above function to determine the number of even items in the list

def isEven(number):
    if number %2:
        return True
    Else:
        return False
