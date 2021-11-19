########################################################################
##
## CS 101 Lab
## Program #Assignment 11
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## create a program to ask a user for hours, minutes and seconds, and create a clock based on that. 
#  Then write a loop that calls tick() once a second and then sleeps for a second.  Use time module to sleep.  
#
# ALGORITHM : 
## Step 1: define class Clock that include 5 perimeters which are self, hour, minute, second, type
## Step 2: in define __self__ takes 1 perimeter, that return in order of hour, minute, second, and "am or pm"
## step 3: ask input from user for hour, minute and second
## Step 4: if hour > 24, return back to 0. 
## Step 5: if second > 60, return back to 0, plus 1 for minute
## Step 6: if minute > 60, return back to 0, plus 1 for hour
## Step 7: use time module
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
import time
class Clock:
    def __init__(self, hour, minute, second, type):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.type = type
        self.timeconvention = ''
    def __str__(self):
        if self.type == 0:
            return "{:02}:{:02}:{:02}{:<2}".format(self.hour, self.minute, self.second,self.timeconvention)
        else:
            if self.hour > 11:
                self.timeconvention = 'pm'
            else:
                self.timeconvention = 'am'
            return "{:02}:{:02}:{:02}{:<2}".format(self.hour, self.minute, self.second,self.timeconvention)
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        elif self.hour > 24:
            self.hour = 0
        elif self.minute == 60:
            self.minute = 0
            self.hour += 1    
def main():
    hours = int(input('What is the current hour ==> '))
    minutes = int(input('What is the current minute ==> '))
    seconds = int(input('What is the current second ==> '))
    clock = Clock(hours, minutes, seconds, 1)
    while True:
        print(clock)
        clock.tick()
        time.sleep(1)
main()
        