#Assignment 8.1
#Tristan Werden
#TODO: None
#NOTES:

#Exercise 1: Write a function called chop that takes a list
#and modifies it, removing the first and last elements, and
#returns None. Then write a function called middle that takes
#a list and returns a new list that contains all but the
#first and last elements.

words = ['a', 'b', 'c']


def chop() :
    words.remove(words[(len(words) - 1)])
    return words.remove((words[0]))

def middle():
    wordsCool = []
    wordsCool.extend(words)
    wordsCool.remove(wordsCool[(len(wordsCool) - 1)])
    wordsCool.remove((wordsCool[0]))
    return wordsCool

print("Middle Function:")
print(middle())
print(words)

print("Chop Function:")
print(chop())
print(words)
