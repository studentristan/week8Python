#Assignment 8.4
#Tristan Werden
#TODO: None
#NOTES:

fh = open('romeo.txt')
words = list()
endWords = list()
for line in fh :
    print(line.rstrip())
    words = line.rstrip().split()
    for word in words : 
        if word not in endWords :
            endWords.append(word)

print(sorted(endWords))