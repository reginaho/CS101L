########################################################################
##
## CS 101 Lab
## Program #Lab Grade Calculator
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
##    This problem is coding a calculator that will be used to calculate
##    grades for the CS101 Lab class using the
##    weighting system which will ask the user to give each of the
##     weighted categories(labs, lab exams and attendance)
##    with grades range from 0 to 100.
## ALGORITHM : 
##      1. Write out the algorithm
##      - Assignmentto a variable
##      - Convert to int and/or float
##      - Calculate values
##      - Get input with the input function
##      - Output results with the print function
##      - Use if, elif and else
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

labs = 0.7
lab_exams = 0.2
attendance = 0.1

print('**** Welcome to the LAB grade calculator! **** \n')

name =str(input('Who are we calculating grades for? ==> '))
print()
labs_grade = int(input('Enter the Labs grade? ==> '))
if labs_grade < 0:
    print('The lab value should have been zero or greater. It has been changed zero.')
    labs_grade = 0
elif labs_grade > 100:
    print('The lab value should have been 100 or less. It has been changed 100.')
    labs_grade = 100
    
print()
exam_grade = int(input('Enter the EXAMS grade? ==> '))
if exam_grade < 0:
    print('The exam value should have been zero or greater. It has been changed zero.')
    exam_grade = 0
elif exam_grade > 100:
    print('The exam value should have been 100 or less. It has been changed 100.')
    exam_grade = 100
print()
attendance_grade = int(input('Enter the Attendance grade? ==> '))
if attendance_grade < 0:
    print('The attendance value should have been zero or greater. It has been changed zero.')
    attendace_grade = 0
elif attendance_grade > 100:
    print('The attendance value should have been 100 or less. It has been changed 100.')
    attendace_grade = 100
print()


weighted = float((labs_grade * labs) + (exam_grade * lab_exams) + (attendance * attendance_grade))
print('The weighted grade for {} is  {}'.format(name,weighted))

if 90 <= weighted <= 100:
    print('{} has a letter grade of A'.format(name))
elif 80 <= weighted < 90:
    print('{} has a letter grade of B'.format(name))
elif 70 <= weighted < 80:
    print('{} has a letter grade of C'.format(name))
elif 60 <= weighted < 70:
    print('{} has a letter grade of D'.format(name))
else:
    print('{} has a letter grade of F'.format(name))

print()
print('**** Thanks for using the Lab grade calculator ****')
    
