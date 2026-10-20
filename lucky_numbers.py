import random

todays_draw = []

available_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def lotto_draw():
    while len(todays_draw) < 3:
        num = random.choice(available_nums)
        if num not in todays_draw:
            todays_draw.append(num)

def get_player_numbers():
    # get 3 numbers from the user "Enter three numbers between 1 and 25 separated by commas. e.g. 5, 10, 15:"
    user_input = input("Enter three numbers between 1 and 25 separated by commas. e.g. 5, 10, 15: ")
    # split the input into a list of strings
    user_numbers = user_input.split(",")
    # convert the list of strings into a list of integers
    # check if the strings are valid numbers between 1 and 25
    for num in user_numbers:
        if len(user_numbers) != 3:
            print("Invalid input. Please enter three numbers between 1 and 25.")
            return get_player_numbers()
        if not num.isdigit() or int(num) < 1 or int(num) > 25:
            print("Invalid input. Please enter three numbers between 1 and 25.")
            return get_player_numbers()

    user_numbers = [int(num) for num in user_numbers]
    print("Your numbers are: ", user_numbers)
    # check if the user numbers are in the todays_draw list
    return user_numbers

def check_numbers(user_numbers):
    matches = []
    for num in user_numbers:
        if num in todays_draw:
            matches.append(num)
    # print the result
    if len(matches) == 0:
        print("Sorry, you didn't match any numbers.")
    elif len(matches) < 3:
        print("You matched " + str(len(matches)) + " number(s): ", matches)
    elif len(matches) == 3:
        print("Wow, you have won the lotto! ", matches)

lotto_draw()
user_numbers = get_player_numbers()
check_numbers(user_numbers)
print("The result of today's draw is........ ", todays_draw)

# The following modifications should be made:
# •	A try-except construct should be added, with the code likely to raise the error placed inside the try block
# •	The except block should explicitly catch the exception raised when the data type conversion isn’t possible
# •	Make sure to supply an alias for the exception
# •	Inside the except block, print out the error message which is stored in the args tuple • We need to handle invalid tickets (Those that don’t have exactly 3 numbers on them). To do this, a custom exception should be created, called InvalidTicketException. After creating the exception class, you can raise the custom exception any time a lotto ticket is being checked with an invalid amount of numbers on it.
# •	You should supply the following message when raising the custom exception:
# ‘Invalid Ticket:  Should contain three numbers’
# •	The custom exception should be raised inside of the try block, and handled by the same except block that is handling the ValueError
# •	A second except block should be added to catch the more general Exception objects when raised. You should again print the error message to the console
# •	The other potential problem was that the user could enter numbers outside the valid range of 1 to 25. We will handle this one using the assert statement. If any of the numbers entered by the user are outside the valid range, the AssertionError will be raised. You can provide the following error message:
#
# ‘This ticket contains numbers that are not in the draw (1 to 25)’
#
# •	If no exceptions are raised, the following statement should be printed before we let the user know how many numbers they got correct:
#
# ‘Thank you for providing your lotto numbers. We will check them now.....’
#
# The app should now be able to handle a variety of inputs appropriately.
