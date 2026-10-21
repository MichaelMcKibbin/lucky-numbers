import random

todays_draw = []

available_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


class InvalidTicketException(Exception):
    pass


def lotto_draw():
    todays_draw.clear()
    todays_draw.extend(sorted(random.sample(available_nums, 3)))
    print("The result of today's draw is........ ")
    print(todays_draw)


def check_numbers():
    while True:
        user_input = input("Enter three numbers between 1 and "+ str(max(available_nums)) + " separated by commas. e.g. 5,10,15: ")
        try:
            user_numbers = [int(num.strip()) for num in user_input.split(",")]
            if len(user_numbers) != 3:
                raise InvalidTicketException("Invalid Ticket:  Should contain three numbers")
            if len(set(user_numbers)) != 3:
                raise InvalidTicketException("Invalid Ticket:  Numbers should be different")
            assert all(1 <= num <= 25 for num in user_numbers), \
                "This ticket contains numbers that are not in the draw (1 to 25)"
        except (ValueError, InvalidTicketException) as error:
            print(error.args[0])
        except Exception as error:
            print(error.args[0] if error.args else error)
        else:
            break

    lotto_draw()
    print("Thank you for providing your lotto numbers. We will check them now.....")
    print("Your numbers are: " + str(user_numbers))
    matches = 0
    for num in user_numbers:
        if num in todays_draw:
            print("***" + str(num) + " was drawn***")
            matches += 1
    print("You matched " + str(matches) + " number(s).")
    if matches == 3:
        print("Wow, you have won the lotto!")


check_numbers()
