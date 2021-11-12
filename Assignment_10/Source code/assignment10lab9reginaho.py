########################################################################
##
## CS 101 Lab
## Program #Assignment 10
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## will ask the user for a text file to read.  You’ll want to read all the words and output a count of the words that are used the most.  
#
# ALGORITHM : 
## Step 1: import operator
## Step 2: take punctuation from string
## step 3: use while loop to ask for the file to open, if it does not exist, tell the user to try again.
## Step 4: read the file, strip the punctuation using for loops, nested for loops.
## Step 5: use if else statement to check if the length of the key is greater or equal to 3.
## Step 6: count both the lower and upper case, return the number of times that the word appears.
## Step 7: count the word that only appear once, and count unique words.
##
#Step 5: print out main()
##
##
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import operator
from string import punctuation

def main():
    while True:
        name = input("Enter the name of the file to open ")
        try:
            with open(name) as file:
                wd = dict()
                for line in file:
                    for word in line.lower().strip().split(" "):
                        word = word.strip(punctuation)
                        if len(word) <= 3:
                            continue
                        else:
                            if word in wd.keys():
                                wd[word] = wd[word] + 1
                            else:
                                wd[word] = 1
                wd = dict(sorted(wd.items(), key=lambda x:x[1], reverse=True))
                appearance = 1
                print("Most frequently used words")
                print("{:>2}{:>20}{:>16}".format('#', 'Word', 'Freq.'))
                print("=====================================")
                for key in wd:
                    if appearance > 10:
                        break
                    else:
                        frequency = wd[key]
                        print("{:>2}{:>20}{:>15}".format(appearance, key, frequency))
                        appearance += 1
                onlyonce = 0
                for key in wd:
                    if wd[key] == 1:
                        onlyonce += 1
                unique = len(wd)

                
                print("There are {} words that occur only once".format(onlyonce))
                print("There are {} unique words in the document".format(unique))

        except:
            print("Could not open file",name)
            print("Please Try Again\n")
            continue
        else:
            break

main()