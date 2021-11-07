########################################################################
##
## CS 101 Lab
## Program #Assignment 9
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## read in a datafile containing crime information for 2019.  
#  create the functions given below with the function signature given.
#  Function signature means the definition of the name of the function as well as any parameters and return values.  
# 
#
# ALGORITHM : 
# Step 1: import csv
# define month_from_number() takes an integer as a parameter 
# and returns a string.  The parameter is expected to be 1 to 12
# and returns the string result for the month.  The list of months is
# January, February, March, April, May, June, July, August, September, October, November, December
# 
# Step 2: define read_in_file() takes a filename as a string and returns a list of list of list of the contents.
# Each sublist is a row from the file
#
# Step 3: define create_reported_date_dict() takes a list, which is the
#  list of lists returned from the read_in_file function above and 
# returns a dictionary where the key is a date of the year found 
# in index 1, and the value is how many times a crime occurred on 
# that data as read from the file
## 
# Step 4: define create_reported_month_dict() takes a list, 
# which is the list of lists returned from the read_in_file
#  function above and returns a dictionary where the key is 
# the month of the offense, and the value is how many times a
#  crime occurred on that data as read from the file.
##
# Step 5: define create_offense_dict()This function takes a list,
# again it is the list returned from read_in_file function 
# and returns a dictionary where the key the offense
# (Arson, Burglary, etc) and the value is how many times that 
# offense occurs.  Offense is column index 7.

# Step 6: define create_offense_by_zip()returns a dictionary
#  where the key the offense (Arson, Burglary, etc)
#  and the value is another dictionary. 
# This sub dictionary has a key for the zip code,
#  and a value that is how many times this offense occurs in this zip code. 
#
# Step 7: use for loop, try and except in the main program and if else.
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

import csv

def month_from_number(n):
    calendar = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
    '07':'July', '08':'August', '09':'September', '10':'October', '11': 'October', '12':'December'}
    if n < '0' or n > '12':
       raise ValueError('Month must be 1-12')
    
    return calendar[n]

def read_in_file(filename):
    data = []
    try:
        file = open(filename,'r',encoding='UTF-8')
        reader = csv.reader(file)

        for row in reader:
            data.append(row)
        file.close()
        return data
    except FileNotFoundError:
        return []
    

def create_reported_date_dict(data):
   date = {}
   for row in data:
       if row[1] in date:
            try:
               date[row[1]] += 1
            except:
                date[row] = 1
            return date
           
def create_reported_month_dict(data):
   month = {}
   for row in data:
       m = row[1][0:2]
       if m in month:
           month[m] += 1
       else:
           month[m] = 1
   return month

def create_offense_dict(data):
   offense = {}
   for row in data:
        key = (row[7].split(' - ')[0])
        if key in offense:
            offense[key] += 1
        else:
            offense[key] = 1
   return offense

def create_offense_by_zip(data):
    offense_by_zip = {}
    for row in data:
        key = (row[7].split(' - ')[0])
        if key in offense_by_zip:
            if row[13] in offense_by_zip[key]:
                offense_by_zip[key][row[13]] += 1
            else:
                offense_by_zip[key][row[13]] = 1
        else:
            offense_by_zip[key] = {row[13]: 1}
    return offense_by_zip


def get_top_ten_key_values(value_dict):
   lst = list(value_dict.items())
   lst.sort(key=lambda x: x[1], reverse=True)
   return lst[:10]

if __name__ == '__main__':
   
   invalid_file = True
   while invalid_file:
    

    file_name = input('Enter the name of the crime data file ==> ')
    lst = read_in_file(file_name)
    if len(lst) > 0: #hoặc là lst != -1
        invalid_file = False
    else:
        print('Could not find the file specified. {} not found'.format(file_name))


       
   
   print()
   months = create_reported_month_dict(lst)
   top_10_months = get_top_ten_key_values(months)
   print('The month with the highest # of crimes is {} with {} offenses'.format(month_from_number(top_10_months[0][0]),top_10_months[0][1]))

   print()
   offenses = create_offense_dict(lst)
   top_10_offenses = get_top_ten_key_values(offenses)
   print('The offenses with the highest # of crimes is {} with {} offenses'.format(top_10_offenses[0][0],top_10_offenses[0][1]))

   offense_by_zip = create_offense_by_zip(lst)

   print()
   invalid_key = True
   while invalid_key:
       offense_key = input('Enter an offense')
       if offense_key in offense_by_zip:
           invalid_key = False
       else:
           print('Not a valid offense found, please try again')

   
   print()
   print('{} offenses by Zip Code'.format(offense_key))
   print('{:20}{:10}'.format('Zip Code','# offenses'))
   print('='*30)
   for key, value in offense_by_zip[offense_key].items():
       print('{:<20}{:>10}'.format(key,value))

