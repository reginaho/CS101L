########################################################################
##
## CS 101 Lab 12
## Program #Assignment 13
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## Unit Testing
# 
#
# ALGORITHM : 
## Import unittest, math, Grades. 
## Create different test functions.
## Create a grade python file to import.
##
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import unittest
import math
import Grades

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    def test_total_returns_zero(self):
        result = Grades.total([])
        self.assertEqual(result,0,"The total function should return 0")
    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result,5.33333,5,"The average should return 5.333")
    def test_average_two(self):
        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result,12.0000,4,"The average should return 12")
    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result,math.nan,"The average should return nan")
    def test_median_returns_one(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result,2,"The median should return 2")
    def test_median_returns_two(self):
        result = Grades.median([5,2,1,3])
        self.assertAlmostEqual(result,2.5,1,"The median should return 2.5")
    def test_median_raise_error(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])
unittest.main()