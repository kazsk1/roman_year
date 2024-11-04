#!/usr/bin/env python

## get_roman_year.py ##

# This script converts a year in numbers to a year in Roman numerals.
# This is intended to check information about a specific year in the Middle Ages.

# Rule 1 #
# I  IV  V  IX  X   L   C    M
# 1  4   5  9   10  50  100  1000

# Rule 2 for using D #
# I  IV  V  IX  X   XL  L   XC  C    CD   D    CM   M
# 1  4   5  9   10  40  50  90  100  400  500  900  1000

# Rule 3 for using j #
# j was typically used in place of the final i in a sequence of i's, 
# as in Roman numerals throughout Middle English. This intends not to add more i.

import sys
import re

def convert_number_to_lower_roman_numeral(number):
    if len(sys.argv) == 3: # 2nd argument #
        if sys.argv[2] == "lowercase" or sys.argv[2] == "l":  # d = 500 & lowercase #
            roman_value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        else: # d != 500 & lowercase using i or j #
            roman_value = [1000, 100, 50, 10, 9, 5, 4, 1]
            roman_char = ["M", "C", "L", "X", "IX", "V", "IV", "I"]
    roman = ''
    for i in range(len(roman_value)):
        while number >= roman_value[i]:
            number -= roman_value[i]
            roman += roman_char[i]
    if sys.argv[2] == "j": # using j #
        lower_roman = re.sub("II$" , "IJ", roman).lower().capitalize()
    else:
        lower_roman = roman.lower().capitalize()
    return lower_roman 

def convert_number_to_upper_roman_numeral(number):
    if len(sys.argv) == 3: # 2nd argument #
        if sys.argv[2] == "d" or sys.argv[2] == "D":  # D = 500 & uppercase #
            roman_value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    if len(sys.argv) == 2: # 1st argument #
        roman_value = [1000, 100, 50, 10, 9, 5, 4, 1]
        roman_char = ["M", "C", "L", "X", "IX", "V", "IV", "I"]
    roman = ''
    for i in range(len(roman_value)):
        while number >= roman_value[i]:
            number -= roman_value[i]
            roman += roman_char[i]
    upper_roman = roman
    return upper_roman 

def main():

    if len(sys.argv) < 2: # no argument #
        print("\033[93mERROR:\033[00m Missing argument. Please add [NUMBERS], add [NUMBERS] d, [NUMBERS] l, [NUMBERS] i, [NUMBERS] j or h.")
        sys.exit(1)

    elif len(sys.argv) > 3: # more than 2nd argument #
        print("\033[93mERROR:\033[00m More than 2nd argument. Please use [NUMBERS], [NUMBERS] d, [NUMBERS] l, [NUMBERS] i, [NUMBERS] j or h.")
        sys.exit(1)

    elif len(sys.argv) == 3: # 2nd argument # 

           if sys.argv[2] == "d" or sys.argv[2] == "D": # uppercase using D # 
               number_input = int(sys.argv[1]) 
               roman_numeral_output = convert_number_to_upper_roman_numeral(number_input)
               print("\033[96mConversion\033[00m")
               print('{0} = {1}'.format(number_input, roman_numeral_output))
               sys.exit()

           if sys.argv[2] == "lowercase" or sys.argv[2] == "l": # lowercase # d = 500 #
               number_input = int(sys.argv[1]) 
               roman_numeral_output = convert_number_to_lower_roman_numeral(number_input)
               print("\033[96mConversion\033[00m")
               print('{0} = {1}'.format(number_input, roman_numeral_output))
               sys.exit()
           
           if sys.argv[2] == "i" or sys.argv[2] == "j": # lowercase using i or j # d != 500 #
               number_input = int(sys.argv[1]) 
               roman_numeral_output = convert_number_to_lower_roman_numeral(number_input)
               print("\033[96mConversion\033[00m")
               print('{0} = {1}'.format(number_input, roman_numeral_output))
               sys.exit()

           else:
               print("\033[93mERROR:\033[00m Invalid 2nd argument. Please use d, l, i or j.")
               sys.exit(1)
    
    
    elif len(sys.argv) == 2: # 1st argument only # 

          if sys.argv[1] == "help" or sys.argv[1] == "h": # help #
              print("")
              print("\033[96m1. Convert Numbers to Roman numerals in uppercase\033[00m")
              print("python3 get_roman_year.py [NUMBERS]")
              print("")
              print("\033[96m2. Convert Numbers to Roman numerals in uppercase using D\033[00m")
              print("python3 get_roman_year.py [NUMBERS] d")
              print("python3 get_roman_year.py [NUMBERS] D")
              print("")
              print("\033[96m3. Convert Numbers to Roman numerals in lowercase using d\033[00m")
              print("python3 get_roman_year.py [NUMBERS] l")
              print("python3 get_roman_year.py [NUMBERS] lowercase")
              print("")
              print("\033[96m4. Convert Numbers to Roman numerals in lowercase not using d\033[00m")
              print("python3 get_roman_year.py [NUMBERS] i")
              print("")
              print("\033[96m5. Convert Numbers to Roman numerals in lowercase not using d / using j\033[00m")
              print("python3 get_roman_year.py [NUMBERS] j")
              print("")
              print("\033[96m6. Show Rules of converting Numbers to Roman numerals\033[00m")
              print("python3 get_roman_year.py r")
              print("python3 get_roman_year.py rules")
              print("")
              print("\033[96m7. Show Help\033[00m")
              print("python3 get_roman_year.py h")
              print("python3 get_roman_year.py help")
              print("")
              sys.exit()

          elif sys.argv[1] == "rules" or sys.argv[1] == "r": # rules #
              print("")
              print("\033[96mRule 1\033[00m")
              print("I  IV  V  IX  X   L   C    M")
              print("1  4   5  9   10  50  100  1000")
              print("")
              print("\033[96mRule 2 for using D\033[00m")
              print("I  IV  V  IX  X   XL  L   XC  C    CD   D    CM   M")
              print("1  4   5  9   10  40  50  90  100  400  500  900  1000")
              print("")
              print("\033[96mRule 3 for using j\033[00m")
              print("j was typically used in place of the final i in a sequence of i's,")
              print("as in Roman numerals throughout Middle English. This intends not to add more i.")
              print("")
              sys.exit()

          elif sys.argv[1].isdigit() == True: # numbers in string only #
              number_input = int(sys.argv[1]) 
              roman_numeral_output = convert_number_to_upper_roman_numeral(number_input)
              print("\033[96mConversion\033[00m")
              print('{0} = {1}'.format(number_input, roman_numeral_output))
              sys.exit()
    
          else:
              print("\033[93mERROR:\033[00m Invalid 1st argument. Please use [NUMBERS], r or h.")
              sys.exit(1)


if __name__ == "__main__":
    main()




