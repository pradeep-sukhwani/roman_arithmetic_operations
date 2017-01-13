import re


# List of numericals to according to their roman apha
numerical = [1000, 900, 500, 400, 100, 90,
             50, 40, 10, 9, 5, 4, 1]
# String of roman aphabets according and then spilting them
roman_apha = "M CM D CD C XC L XL X IX V IV I".split()

# created a dictionary of keys to numerical and
# value of roman_apha and zipping them. Means creating a dictionary of lists
numerical_roman = dict(zip(numerical, roman_apha))


def roman_to_numeric(user_input):
    '''verify and convert Roman aphabets to numericals'''
    if (verify_roman(user_input)):
        user_input = user_input.upper()
        number = 0
        for num, rom in zip(numerical, roman_apha):  # looping in global dic
            while user_input.startswith(rom):  # starswith is a python method
                # which checks that the first digit/aphabet is roman or not
                number += num  # incrementing the value of number by num
                user_input = user_input[len(rom):]
        return number  # return the number
    else:
        return -1  # else returning -1


def verify_roman(user_input):
    '''Regular expression to check the user input is roman or not'''
    regular_exp = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
    if user_input == "":
        return False
        # if user_input is roman verifying using regular_exp then it will
        # return True then will be used in roman_to_numeric function else false
    if re.match(regular_exp, user_input, re.IGNORECASE):
        return True
    else:
        return False


def arithmetic_operations(user_input):
    '''Verify that numeric is not 0 and not greater than 3999 to Roman
    plus the calculation part where actually the arithmetic operations
    are done'''
    result = ""  # creating an empty variable of sting with name result
    # which contains only romans
    user_input_integer = int(user_input)
    if (verify_numeric(user_input_integer)):  # verify that no. is less
        # and 3999 greater then 0
        for num in numerical:  # looping in list of global numericals
            while user_input_integer >= num:
                result += numerical_roman[num]  # incremeting the value of
                # result or putting value in result with lists of dictionary
                user_input_integer -= num  # decrement the value got from
                # user_input with number i.e. num
        if user_input_integer != 0:  # make sure value is not zero
            result += numerical_roman[num]  # then incrementing the value of
            # result with list of dictionary
        return "Result: " + result  # returing the output result
        # numeric form not roman form


def verify_numeric(n):
    '''verify that if 3999 or less than 0 will return false else true
    if true then it will be used in numeric to roman function'''
    if (n > 3999 or n < 0):
        return False
    else:
        return True


def numeric_to_roman():
    '''Converting the numeric form got from arithmetic_operations function
    to Roman Alphabet'''
    # taking input from user
    user_input = raw_input("Please enter the roman aphabets: ")
    regex = re.split(r'([+*/-])', user_input)  # spliting the regular
    # expression from user_input
    expression = ''
    for roman in regex:  # looping in regex
        if (verify_roman(roman)):  # if input is roman apha
            expression += str(roman_to_numeric(roman))  # then adding
            # to expression as a str
        else:
            expression += str(roman)  # adding roman apha as a str in
    # expression
    roman_value = (eval(expression))  # using eval function for getting
    # roman apha
    return arithmetic_operations(roman_value)  # calling arithmetic_operation
    # function with roman value to return the calculated roman alpha


#  Add test functions
if __name__ == "__main__":
    print numeric_to_roman()
