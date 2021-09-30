########################################################################
##
## CS 101 Lab
## Program #Assignment 4
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
##      Simulate a slot machine in Pierson Hall. The slot machine has 3 reels and each reel will have numbers ranging from 1 to 10.   
##      The user can choose how many chips they start out with.   
##      They are allowed to wager between 1 to the amount of bank they currently have on each spin.    
##      If they match 3 numbers, they will win 10 times their wager.  If they match 2 numbers they will win 3 times their wager. 
## ALGORITHM : 
##      1.Write out the algorithm
####Step 1: define function play_again()-> Boolean
##create list = [‘all yes no with lowercases, and uppercases’]
##play = input('Do you want to play again? ==>')
##    if input for play == ‘yes’(regardless of case) return True
##    if input for play not in list return play_again
##return false otherwise
##
#### Step 2: define get_bank() to start the program 
##chips = input()
##if chips < 1, print(‘Too low a value’) ; if chips > 100, print (‘Too high a value’)
##         return get_bank()
##return chips otherwise
##
#### Step 3:  define get_wager(bank):
##chips = input()
##if chips < 1, print(‘the wager amount must be greater than 0) ; if chips > bank, print (‘The wager amount cannot be greater than how much you have. (bank))
##          return get_wager(bank)
##return chips otherwise
##
#### Step 4 : import random
##define get_slot_results ():
##    reel1 = random.randint(1,10)
##    reel2 = random.randint(1,10)
##    reel3 = random.randint(1,10)
##    return reel1, reel2, reel3
##
#### Step 5: define get_matches(reela,reelb,reelc):
##return 3 if reela == reelb == reelc
##return 2 if reela==reelb or reela==reelc or reelb==reelc
##return 0 otherwise
##
#### Step 6: define get_payout(wager,matches):
##return wager * 10 – wager if matches == 3
##return wager * 3 – wager if matches == 2
##return wager * -1 otherwise
##
#### Step 7:  declare if __name__=="__main__": (contains anything in the main portion of the program)
##playing = True
##while playing:
##         bank = get_bank()
##         begin_chips = bank
##         most = bank
##         count = 0
##         while True:
##                wager = get_wager(bank)
##                reel1,reel2,reel3 = get_slot_results()
##                matches = get_matches(reel1,reel2,reel3)
##                payout = get_payout(wager,matches)
##                bank = bank  + payout
##                print("Your spin",reel1,reel2,reel3)
##                print("You matched",matches,"reels")
##                print("You won/lost",payout)
##                print("Current bank",bank)
##                print()
##                count = count + 1
##                if most < bank:
##                     most = bank
##                if bank < 1:
##                     break
##         print("You lost all",begin_chips,"in",count,"spins")
##         print("The most chips you had was",most)
##         playing = play_again()
##
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import random
def play_again():
    play = input("Do you want to play again? ==> ")
    lst = ['y','Y','YES','yEs','YEs','YeS','Yes','No','no','n','NO','yes','yES','yeS']
    if play not in lst:
        print()
        print('You must enter Y/YES/N/NO to continue.   Please try again')
        return play_again()
    elif play == 'y' or play == 'Y' or play == 'Yes' or play == 'YES' or play == 'YeS' or play == 'YEs' or play == 'yEs' or play == 'yes':
        return True
    return False

def get_bank():
    chips = int(input('How many chips do you want to start with? ==> '))
    if chips < 1:
        print('Too low a value, you can only choose 1 - 100 chips')
        return get_bank()
    elif chips > 100:
        print('Too high a value, you can only choose 1 - 100 chips')
        return get_bank()
    return chips

def get_wager(bank):
    chips = int(input('How many chips do you want to wager? ==> '))
    if chips < 1:
        print('The wager amount must be greater than 0.  Please enter again.')
        return get_wager(bank)
    elif chips > bank:
        print('The wager amount cannot be greater than how much you have.  {}'.format(bank))
        return get_wager(bank)
    return chips
    
def get_slot_results():
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)
    return reel1, reel2, reel3

def get_matches(reela,reelb,reelc):
    if reela == reelb == reelc:
        return 3
    elif (reela==reelb or reela==reelc or reelb==reelc):
        return 2
    return 0
        
def get_payout(wager,matches):
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager* 3 - wager
    return wager * -1

if __name__=="__main__":
    playing = True
    while playing:
        bank = get_bank()
        begin_chips = bank
        most = bank
        count = 0
        while True:
            wager = get_wager(bank)
            reel1,reel2,reel3 = get_slot_results()
            matches = get_matches(reel1,reel2,reel3)
            payout = get_payout(wager,matches)
            bank = bank + payout
            print("Your spin",reel1,reel2,reel3)
            print("You matched",matches,"reels")
            print("You won/lost",payout)
            print("Current bank",bank)
            print()
            count = count + 1
            if most < bank:
                most = bank
            if bank < 1:
                break
        print("You lost all",begin_chips,"in",count,"spins")
        print("The most chips you had was",most)
        playing = play_again()