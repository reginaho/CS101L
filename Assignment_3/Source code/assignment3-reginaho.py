########################################################################
##
## CS 101 Lab
## Program #Assignment 3
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
##      The great prognosticator “Flarsheim”, will let the user choose a number in their head from 1 to 100. 
##      It will then ask the remainder of this number when divided by 3, 5 and 7. 
##      The program must validate proper input on each.  The remainder when divided by 3 can only be 0, 1 or 2.  
##      The remainders for 5 and 7 are different.  
##      Find the number from 1 to 100 that has the same remainder for 3, 5, and 7 
##      and astound them with the result which will be the number that the player is thinking about.
##      They are then asked if they want to play again.  The player may enter Y or N only.
##
## ALGORITHM : 
##      1. Write out the algorithm
## Step 1: print('Welcome to the Flarsheim Guesser!\n')
## Step 2: define choice as choice = 'Y' to create choice as the player's input for yes or no later on.
## Step 3: create a while loop that will run to guess the player's number when they start the program or input 'y' or 'Y'
## Step 4: inside the while loop will include : ask the player to think of a number between 1 and 100, create a dictionary
## that includes '357', create an empty list to use later with the index 'i'.
## Step 5: create a while loop inside the above while loop that will run and get the input from the player about the remainder.
## Step 6: create if-else-if that will print out the input or check of the value enter is valid.
## Step 7: need to check for the range of 'x' which is the number of the player, if the modulo of 3,5,7 is valid, and print that number.
## Step 8: break from the loop
## Step 9: ask for the player's choice if they want to continue or not.
## Step 10: loop if the input is not 'y', 'Y', 'n', or 'N', until the valid input is given.
## Step 11: run again if is it 'y' or 'Y', exit the program if the input is 'n' or 'N'.
## Step 12: stop and exit.
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

print('Welcome to the Flarsheim Guesser!\n')

choice = 'Y'
while choice.lower() == 'Y' or choice.lower() == 'y':
    print()
    print('Please think of a number between and including 1 and 100')
    print()
    numbers357 = '357'
    lst = []
    for i in numbers357:
        while True:
            print("What is the remainder when your number is divided by",i,"?",end=' ')
            remainder = int(input())
            if remainder < 0:
                print("The value entered must be 0 or greater")
                continue
            elif remainder >= int(i):
                print("Th-e value entered must be less than",i)
                continue
            else:
                if i!= '7': 
                    print()
                lst.append(remainder)
                break
    for x in range(1,101):
        if(x%3 == lst[0] and x%5 == lst[1] and x%7 == lst[2]):
            print("Your number was ",str(x))
            print("How amazing is that?\n")
            break
    choice=input("Do you want to play again? Y to continue,N to quit ==> ")
    while(choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n' ):
        choice=input("Do you want to play again? Y to continue,N to quit ==> ")
        