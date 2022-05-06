fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
words = list()
fh = open(fname)

count = 0

for line in fh :
    words = line.split()
    if (len(words) > 0):
        if ((words[0] == 'From') & (words[0] != 'From:')) :
            print(words[1])
            count = count + 1

print("There were", count, "lines in the file with From as the first word")