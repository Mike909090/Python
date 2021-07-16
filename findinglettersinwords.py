#make a string
GSttring = 'Gone are the goners, they gave us the givings'
#word you will use to compare
gword = 'g'
#initialize counter variable that will be used to add on letters
counter = 0
#loop through the word and find a letter and add it to the counter
for gword in GSttring:
    if gword == 'g':
        counter+=1
#print the counter
print(str(counter))
