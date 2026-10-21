# Lucky Numbers

A small Python command-line lottery app based on Exercise 2 of **PCAP Topic 2 Exercises**. It draws three unique numbers from 1 to 25, asks the player for a ticket, and reports how many numbers match.

## Requirements

- Python 3
- No third-party packages

## Run the app

From the repository directory, run:

```
python lucky_numbers.py
```

When prompted, enter exactly three different numbers between 1 and 25, separated by commas. Spaces around the numbers are accepted. For example:

```
5, 10, 15
```

The app first asks for a ticket. It rejects non-numeric entries, tickets without exactly three numbers, duplicate numbers, and numbers outside 1–25, then asks again. Once the ticket is valid, the draw takes place and the sorted result is printed. The app then prints a thank-you message, `***N was drawn***` for each match, the number of matches, and a congratulation if all three match.

## Project files

- `lucky_numbers.py` — lottery draw, ticket input, validation, and match reporting.
- `PCAP Topic 2 Exercises.txt` — the assignment brief, including the Ambianese exercise and the full lotto exercise requirements.  

Ticket validation uses `ValueError` handling for non-numeric input, a custom `InvalidTicketException` (handled in the same `except` block) for the wrong number of entries or duplicates, an `assert` for values outside 1–25, and a general `except Exception` fallback, as requested in the exercise brief.
