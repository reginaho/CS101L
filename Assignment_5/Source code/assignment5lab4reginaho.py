########################################################################
##
## CS 101 Lab
## Program #Assignment 5
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
# The Linda Hall library wants to come up with a new library card numbering system for students.
# The card number’s first 5 characters are A-Z, which will normally be the first five characters of the student’s name.
# The next character at index 5 is a string value either 1, 2, or 3 which represents the different schools; SCE, School of Law,
# or College of arts and Sciences.  The character at index 6 is either 1, 2, 3, or 4. 
# These are the grade levels; Freshman, Sophomore, Junior, and Senior. 
# The next 2 characters are 0-9, and the last character at index 9 is the check digit to verify the previous values.  
# The last character is also 0-9.
#
## ALGORITHM : 
##      1.Write out the algorithm
#
#  Step 1: print(‘Linda Hall’) with centered and format. 
# Print(‘Library Card Check’) with centered and format
# Print = * 50

# Step 2 : define get_school(lib_card):
# return 'School of Computing and Engineering SCE' if index 5 == ‘1’
# return ‘School of Law’ if index 5 == ‘2’
# return ‘College of Arts and Sciences’ if index 5 == ‘3’
# else : return ‘Invalid School’
 
# Step 3: define get_grade(lib_card):
# return ‘Freshman' if index 6 == ‘1’
# return ‘Sophomore ‘ if index 6 == ‘2’
# return ‘Junior’ if index 6 == ‘3’
# return ‘Senior’ if index 6 == ‘4’
# else : return ‘Invalid Grade’

# Step 4:  define character_value(c):
# c_value = orc(c)
# return c_value – 65(to convert it to be a 0) if c_value >= 65 and c_value <= 90
# return c_value-48(to convert it to be a 0) if c_value >=48 and c_value <=57

# Step 5 : define get_check_digit(lib_card):
# sum of all values at indexes from 0-8.
# For loop:
#      value = value * index+1
#      sum = (sum + value) % 10
# return sum

# Step 6: define verify_check_digit(lib_card):
# return False and print(‘The length of the number given must be 10) if len(lib_card) != 10

# for i in range(5):
#        if not [A – Z]:
#              return False and print(‘The first 5 characters must be A-Z, the invalid character is at str(i) + " is " + lib_card[i])

# for i in range(7,10):
#        if not [0-9]:
#              return False and print(The last 3 characters must be 0-9, the invalid character is at str(i) is lib_card[i])"

# return False and print(‘The sixth character must be 1 2 or 3) if lib_card[5] !=’1’ and != ‘2’ and != ‘3’ 

# return False and print(‘The seventh character must be 1 2 3 or 4) if lib_card[6] !=’1’ and != ‘2’ and != ‘3’ and != ‘4’

# lib_card[9] != calculated check digit of [lib_card]
# return False and print(‘Check digit {} does not match calculated value {}’.format(int(lib_card[9], calculated)

# return True if library card is valid and check digit matches

# Step 7:  declare if __name__=="__main__": (contains anything in the main portion of the program)
# While True:
# lib_card = input('Enter Library Card. Hit Enter to Exit ==> ')
#         if lib_card ==  '':
#             break

#         valid = verify_check_digit(lib_card)
        
#         if valid == True:
#             print('The card belongs to a students in {}'.format(get_school(lib_card)))
#             print('The card belongs to a {}'.format(get_grade(lib_card)))
#             print()
#         else:
#             print()
#
# Step 8: stop
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
print('{:^50}'.format('Linda Hall'))
print('{:^50}'.format('Library Card Check'))
print('=' *70)

def get_school(lib_card):
    if lib_card[5]== '1':
        return 'School of Computing and Engineering SCE'
    elif lib_card[5] == '2':
        return 'School of Law'
    elif lib_card[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(lib_card):
    if lib_card[6] == '1':
        return 'Freshman'
    elif lib_card[6] == '2':
        return 'Sophomore'
    elif lib_card[6] == '3':
        return 'Junior'
    elif lib_card[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value(c):
    c_value = ord(c)
    if c_value >= 65 and c_value <= 90:
        return c_value -65
    elif c_value >= 48 and c_value <= 57:
        return c_value - 48

def get_check_digit(lib_card):
    sum = 0
    for i in range(len(lib_card)):
        value = character_value(lib_card[i])
        sum = sum + value * (i+1)
    return sum % 10

def verify_check_digit(lib_card):
    if len(lib_card) != 10:
        print('Library card is invalid')
        print('The length of the number given must be 10')
        return False
        
        
    for i in range(5):
        if lib_card[i] < 'A' or lib_card[i] >'Z':
            print('Library card is invalid')
            print('The first 5 characters must be A-Z, the invalid character is at ' + str(i) + " is " + lib_card[i])
            return False
    for i in range(7,10):
        if lib_card[i] < '0' or lib_card[i] > '9':
            print('Library card is invalid')
            print('The last 3 characters must be 0-9, the invalid character is at' + str(i) + "is" + lib_card[i])
            return False
    if lib_card[5] != '1' and lib_card[5] != '2' and lib_card[5] != '3':
        print('Library card is invalid')
        print('The sixth character must be 1 2 or 3')
        return False
    if lib_card[6] != '1' and lib_card[6] != '2' and lib_card[6] !='3' and lib_card[6] != '4':
        print('Library card is invalid')
        print('The seventh character must be 1 2 3 or 4')
        return False
    
    calculated_value = get_check_digit(lib_card)
    given = int(lib_card[9])
    if given != calculated_value:
        print('Library card is invalid')
        print('Check digit {} does not match calculated value {}.'.format(given,calculated_value))
        return False

    print('Library card is valid')
    return True



if __name__=="__main__":
    while True:
        lib_card = input('Enter Library Card. Hit Enter to Exit ==> ')
        if lib_card ==  '':
            break

        valid = verify_check_digit(lib_card)
        
        if valid == True:
            print('The card belongs to a students in {}'.format(get_school(lib_card)))
            print('The card belongs to a {}'.format(get_grade(lib_card)))
            print()
        else:
            print()
            
            