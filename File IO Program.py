"""
first line opens the data file
second line creates the averages file for final output
"""

datafile = open('data.txt', 'r')
average = open('averages.txt', 'w')

"""
a for loop that reads returns each item in the text file as a list...
the split function splits each item in the list so that
the program knows when it reaches a new student
"""
#create a variable that is already assigned to read each line in the data txt
line = datafile.read().split('\n')
#an empty string for writing in the new file
newfile = ''

for l in line:
    #need a counter for the sum of grades
    sumgrades = 0.0
    #need a counter so that the computer increments the grades at some point
    nextgrade = 0.0
    #need a variable that is already assigned to retrieve every WORD in the entry
    words = l.split('\t') #\t because the format requires that the info be split by tabs
    """
    creates an if statement that checks if the line has content or not
    """
    if len(words) >= 2:
        firstN = words[0]
        lastN = words[1]
        fullN = firstN + ' ' + lastN
        #create a variable that helps the computer stop at a name
        #the same variable should return a list with empty strings and grades
        grades = l.split(firstN + '\t' + '\t') #make sure to put tabs!
        #check for any contradctions or exceptions
        if len(grades) == 2:
            g = grades[1]
            singlegrade = g.split('\t') #those darn tabs
            for grade in singlegrade:
                sumgrades += float(grade)
                nextgrade += 1
                newfile += fullN + ': ' + str(sumgrades / nextgrade) + '\n'
            averages.write(newfile)
datafile.close()
average.close()
