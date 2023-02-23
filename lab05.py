########################################################################
##
## CS 101 Lab
## Program # 05
## Name: Riley Connors
## Email: rpczdb@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

import string

# functions

def get_school(string):
    if string[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif string[5] == '2':
        return 'School of Law'
    elif string[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(card_no):
    if card_no[6] == '1':
        return 'Freshman'
    elif card_no[6] == '2':
        return 'Sophomore'
    elif card_no[6] == '3':
        return 'Junior'
    elif card_no[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value(string):
    return ord(string) - 65

def get_check_digit(card_no):
    sum_letters = 0
    for i in range(5):
        sum_letters += character_value(card_no[i]) * (i + 1)

    sum_nums = 0
    for i in range(5, 9):
        sum_nums += int(card_no[i]) * (i + 1)

    total_sum = sum_letters + sum_nums

    return total_sum % 10

def verify_check_digit(card_no):

    truth = True
    reason = ""
    if len(card_no) != 10:
        truth = False
        reason = "The length of the number given must be 10"
        return truth, reason

    if card_no[0:5].isalpha() != True:
        truth = False
        for i in card_no[0:5]:
            if i.isalpha() != True:
                reason = f'The first 5 characters must be A-Z, the invalid character is at {card_no.index(i)} is {i}' 
        return truth, reason

    if card_no[7:10].isnumeric() != True:
        truth = False
        for i in card_no[7:10]:
            if i.isnumeric() != True:
                reason = f'The last 3 characters must be 0-9, the invalid character is at {card_no.index(i)} is {i}' 
        return truth, reason

    if card_no[5] not in ['1', '2', '3']:
        truth = False
        reason = "The sixth character must be 1 2 or 3"
        return truth, reason

    if card_no[6] not in ['1', '2', '3', '4']:
        truth = False
        reason = "The seventh character must be 1 2 3 or 4"
        return truth, reason

    if get_check_digit(card_no) != int(card_no[9]):
        truth = False
        reason = f'Check Digit {card_no[9]} does not match calculated value {get_check_digit(card_no)}.'
        return truth, reason

    return True, ""

if __name__ == "__main__":

    card_no = input('Enter Library Card. Hit Enter to Exit ==> ')

    while card_no:
        if verify_check_digit(card_no)[0] == True:
            print('Library card is valid.')
            print(f'The card belongs to a student in {get_school(card_no)}')
            print(f'The card belongs to a {get_grade(card_no)}')
            print()
            card_no = input('Enter Library Card. Hit Enter to Exit ==> ')
        else:
            print('Library card is invalid')
            print(verify_check_digit(card_no)[1])
            print()
            card_no = input('Enter Library Card. Hit Enter to Exit ==> ')
        
    
    # main program
    print("Main Program")

