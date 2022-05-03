#Assignment 8.2
#Tristan Werden
#TODO: None
#NOTES: If there is a space in their email username, it skips ahead to the day

fhand = open('mbox-short.txt')
count = 0
daysSet = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'}
days = list(daysSet)
for line in fhand:
    wordsList = line.split()
    words = list(wordsList)
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] == 'From' :
        for i in range(0, 7, 1) :                               #I tried to use 2 c-style for loops. Apparently that's not allowed.
            for j in range((len(words) - 1), 0, -1) :                 #First language I've ever EVER had that syntax be different in.
                if (words[j]) == (days[i]) :
                    print(words[j])
                else : continue
