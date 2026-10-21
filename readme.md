# Lucky Numbers

A small Python command-line lottery app. 
It draws three unique numbers from 1 to 25, asks the player to choose 3 numbers, and reports how many numbers match.

## Requirements

- Python 3
- No third-party packages

## Run the app

From the repository directory, run:

```
python lucky_numbers.py
```

When prompted, enter exactly three different numbers between 1 and 25, separated by commas. For example:

```
5,10,15
```
or
```
5, 10, 15
```

- The app asks the user for 3 numbers.
- It can handle spaces between numbers and commas,
- It rejects non-numeric entries, 
- It rejects entries without exactly three numbers, 
- It rejects duplicate numbers, 
- It rejects numbers outside the range 1–25, 
- If the entry is rejected, the app asks the user to try again. 
- After a valid entry is provided, the draw takes place and the sorted result is printed. 
- The app then prints a thank-you message, `***N was drawn***` for each match, the number of matches, and a congratulation if all three match.

## Project files

`lucky_numbers.py` — lottery draw, ticket input, validation, and match reporting.

Ticket validation uses `ValueError` handling for non-numeric input, a custom `InvalidTicketException` (handled in the same `except` block) for the wrong number of entries or duplicates, an `assert` for values outside 1–25, and a general `except Exception` fallback, as requested in the exercise brief.
