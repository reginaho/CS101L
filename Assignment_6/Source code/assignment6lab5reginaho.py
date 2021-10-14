########################################################################
##
## CS 101 Lab
## Program #Assignment 6
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
#Caesar Ciper : write a utility that Encodes and Decodes a Cipher
#
# ALGORITHM : 
# ##      1. Write out the algorithm
# Step 1: import string

# Step 2 : define Encrypt(string_text, int_key)
# cipher_e = ‘’
# for loop:
# for i in range(len(string_text):
#      ch = string_text[i]
#   return cipher_e += chr((ord(ch) + int_key -65) % 25 +65) if is it an uppercased string.
#   return the same but -97 and + 97 if it is a lowercased string.
#   return ch otherwise.
# return cipher_e
 
# Step 3: define Decrypt(string_text, int_key):
# cipher_d = ‘’
# for loop:
# for i in range(len(string_text):
#      ch = string_text[i]
#   return cipher_d += chr((ord(ch) + int_key -65) % 25 +65) if is it an uppercased string.
#   return the same but -97 and + 97 if it is a lowercased string.
#   return ch otherwise.
# return cipher_d

# Step 4:  define Get_input():
# Return the selection of 1,2 or Q of the user’s choices.

# Step 5 : define Print_menu():
# Print the whole menu with option 1 is Encode a string, 2 is Decode a string and Q is Quit.

# Step 6: define main():
# While loop to keep asking until the user choose Q(to quit):
#    Print the menu
#    Choice = Get_input()
#     If Choice == 1, return the encrypt option, and the number to shift letters by.
#     If Choice == 2, return the decrypt option, and the number to shift letters by.
#     Return ‘have an ordinary day’ otherwise.

# Step 7: main() outside of all functions.
##
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
import string 

def Encrypt(string_text, int_key): 
  cipher_e = ''
  for i in range(len(string_text)):
    ch = string_text[i]
    if ch.isupper():
      cipher_e += chr((ord(ch) + int_key - 65) % 26 + 65)
    elif ch.islower():
      cipher_e += chr((ord(ch) + int_key - 97) % 26 + 97)
    else:
      cipher_e += ch
  return cipher_e


def Decrypt(string_text, int_key):
  cipher_d = ''
  for i in range(len(string_text)):
    ch = string_text[i]
    if ch.isupper():
      cipher_d += chr((ord(ch) - int_key - 65) % 26 + 65)
    elif ch.islower():
      cipher_d += chr((ord(ch) - int_key - 97) % 26 + 97)
    else:
      cipher_d += ch
  return cipher_d
  
 
def Get_input():
  user_choice = str(input('Enter your selection ==> '))
  return user_choice
  

def Print_menu():
  print()
  print("MAIN MENU")
  print("1) Encode a String")
  print("2) Decode a String")
  print("Q) Quit")
  
  
def main(): 
  Again = True
  while Again:
    Print_menu()
    Choice = Get_input()
    if Choice == '1': 
      print()
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      print()
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext)
    else: 
      print("Have an ordinary day.") 
      Again = False
    
    
  
      
      
# our entire program:

main()
