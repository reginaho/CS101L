########################################################################
##
## CS 101 Lab
## Program #Assignment 7
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## read through a file containing information about fuel economy and output the results to a file above a threshold that the user gives.
#
# ALGORITHM : 
# Step 1: define get_min_mpg(): which will get the input of the minimum mpg, only in between 0 and 100, if out of range, warn the user, and
## warn the user if they do not enter a number (ValueError) and ask until the enter the right value.
# 
# Step 2: define get_input_file(): get the input as the name of the input vehicle file. Read through the file if exists, if not, return 'Could not
## read the file'. Ask until the user gives the right file.
##
# Step 3: define write_to_file(): get the input as the name of the file to output to. Print the information into a new file.
## Use while loop. Use try and except to print the information. Try will contain open file, read file and write a new file with the correct spaces.
## Except will return False if could not convert value to stop the program.
##Also, may use nested try and except to evaluate Errors.
## 
# Step 4: define main(): all statement that is outside of all functions above.
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
def get_min_mpg():
    while True:
        try:
            min_mpg=float(input("Enter the minimum mpg ==> "))
            if min_mpg<0:
                print('Fuel economy given must be greater than 0')
            elif min_mpg>100:
                print('Fuel economy must be less than 100')
            else:
                print()
                return min_mpg
                
        except ValueError:
            print('You must enter a number for the fuel economy')


def get_input_file():
    while True:
        need_file=input('Enter the name of the input vehicle file ==> ')
        try:
            with open(need_file,'r') as read_file:
                print()
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]
                
        except:
            print('Could not open file',need_file)

def write_to_file(min_mileage,file_data):
    while True:
        new_file = input('Enter the name of the file to output to ==> ')
        print()
        try:
            with open(new_file,'w') as write_file:
                for data in file_data:
                    try:
                        if min_mileage>=float(data[7]):
                            write_file.write('{:<5}{:<40}{:<40}{:>10.3f}\n'.format(data[0],data[1],data[2],float(data[7])))
                    except:
                        print('Could not convert value {} for vehicle'.format(data[7]),data[0],data[1],data[2])
                write_file.close()       
                return False
                
        except:
            print('There is an IO Error',new_file)
    

def main():
    min_mileage=get_min_mpg()
    file_data=get_input_file()[1:]
    write_to_file(min_mileage,file_data)
    
    
main()


