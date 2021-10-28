########################################################################
##
## CS 101 Lab
## Program #Assignment 8
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## Grade weighting.  Our program will allow the user to enter 2 types of grades; Tests and Programs.  
## Each of our scores is assumed to be out of 100, so we only need the users score.
## The tests are 60% of a student’s grade, while the assignments are 40%.  
## In order to calculate the final score, we multiply the mean score of the tests by 0.6 and add it to the mean of assignments multiplied by 0.4.
#
# ALGORITHM : 
# Step 1: define grademenu() which is the menu with 6 options.
# 
# Step 2: define user_input() that will get the input from the user that will select 1 in 6 options provided.
##
# Step 3: define mean() which returns the mean of scores(total/sum)
## 
# Step 4: define std() which returns the the standard deviation(taking each value and subtracting the mean, and squaring the value.  
# Divide the sum of those values by the numbers of values, and take the square root of that result)
##
# Step 5: define display(2 parameters which will be test score and assignment scores) that will print out the display of the scores
##
# Step 6: define main() with all main function that needed.
# Create dictionaries that will store all the scores that we get from the user.
# return append( test score ) if the user chooses 1
# return remove one test score if the user chooses 2, warn them if could not find the score the user enters.
# return clear all the test score if the user chooses 3
# return append( assignment score ) if the user chooses 4
# return remove one assignment score if the user chooses 5, warn them if could not find the score the user enters.
# return clear all the assignment score if the user choose 6
# return display() if the user chooses d or D
# return exit the program if the user chooses q or Q
# uses while loop to repeat the program if needed
#
# Step 7: call main() to run the function
#
##
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def grademenu():
    print('           Grade Menu')
    print('1 - Add Test')
    print('2 - Remove')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Ckear Assignments')
    print('D - Display Scores')
    print('Q - Quit')

def user_input():
    user_input = str(input('=>> '))
    return user_input


def mean(a):
    if len(a) == 0:
        return 0
    else:
        sum = 0.0
        for i in a:
            sum += i
        return sum/len(a)


def std(mean,a):
    sqrt_sum = 0.0
    for i in a:
        sqrt_sum += (i - mean) ** 2
    return (sqrt_sum/len(a)) ** 0.5


def display(test,a):
    num_test = len(test)
    num_a = len(a)
    weighted = 0.00
    print('Type               #       min       max       avg       std')
    print('=' * 61)
    if num_test == 0:
        print()
        print('Tests              0       n/a       n/a       n/a       n/a')
    else:
        test_min = min(test)
        test_max = max(test)
        test_avg = mean(test)
        test_std = std(test_avg, test)
        weighted += test_avg * 0.6
        print('Tests              {}      {:.1f}      {:.1f}      {:.2f}      {:.2f}'.format(num_test, test_min, test_max, test_avg, test_std))
    if num_a == 0:
        print('Programs           0       n/a       n/a       n/a       n/a')        
    else:
        a_min = min(a)
        a_max = max(a)
        a_avg = mean(a)
        a_std = std(a_avg, a)
        weighted += a_avg*0.4
        print('Programs           {}      {:.1f}      {:.1f}      {:.2f}      {:.2f}'.format(num_a, a_min, a_max, a_avg, a_std))
    print()
    print('The weighted scores is       {:.2f}'.format(weighted))
    

def main():
    test_scores = []
    a_scores = []
    while True:
        print()
        grademenu()
        print()
        Choice = user_input()
        if Choice == '1': 
            print()
            new = float(input("Enter the new Test score 0-100 ==> "))
            while new < 0:
                new = float(input("Enter the new Test score 0-100 ==> "))
            test_scores.append(new)
            
        elif Choice == '2': 
            print()
            new = float(input("Enter the new Test score 0-100 ==> "))
            grade_remove = False
            for i in test_scores:
                if i == new:
                    test_scores.remove(new)
                    grade_remove = True
            if grade_remove == False:
                print('Could not find that score to remove')
        
        elif Choice == '3': 
            test_scores.clear()
            
        elif Choice == '4':
            print()
            new = float(input("Enter the new Assignment score 0-100 ==> "))
            while new < 0:
                new = float(input("Enter the new Assignment score 0-100 ==> "))
            a_scores.append(new)
            
        elif Choice == '5': 
            print()
            new = float(input("Enter the new Assignment score 0-100 ==> "))
            grade_remove = False
            for i in a_scores:
                if i == new:
                    a_scores.remove(new)
                    grade_remove = True
            if grade_remove == False:
                print('Could not find that score to remove')
        elif Choice == '6': 
            a_scores.clear()
        elif Choice == 'D' or Choice == 'd':
            display(test_scores, a_scores)
        elif Choice == 'Q' or Choice == 'q':
            break
        else:
            print('Please choose correct option')


main()
