# LocalSanta

Secret Santa, but only give gifts to people you actually know.

This pseudo-random programs works best for groups of size 12-30.

## Inputs

3 types of inputs are accepted with formats (values can have starting/trailing spaces; they will be stripped):

1. `.csv` ↣ Example - 2 rows of a file:

| Goku,Vegeta, Gohan     |
|------------------------|
| Edward, Alphonse,Winry |

2. `.xlsx` ↣ An Excel file where the first cell of each row is a person and the remaining cells in that row are people they might gift.

3. `.json` ↣ A JSON file where each key is a person and the value is a list of people they might want to give a gift.

***NOTE***: Names must be unique! ("Bruce" and "Bruce Wayne" refer to same person irl, but the program will treat them as same person)

## Setup & Execution

You only have to run this `pip install` in case you have your data provided in `.xlsx` (Excel) format:

`pip install openpyxl`

To run the program, pass the filename as an argument to `main.py`:

`python main.py INPUT_FILE`

## Algorithm

The program uses a randomized greedy algorithm with retries to assign Secret Santa pairs.

**Core Strategy:** Sort people by how many gift recipients they can choose from (smallest first), then randomly assign recipients one by one. If anyone runs out of options, restart from scratch and try again. People with fewer choices are most likely to get stuck with no valid options. By handling them first, we maximize the chance they get someone before their options are taken. People with many choices are flexible and can work with whatever's left.

**The Process:**

1. Sort all gifters by their recipient list size (ascending)
2. For each gifter in order:
   - Filter their recipient list to remove people already assigned
   - If no one is available, this attempt fails
   - Otherwise, randomly pick someone from available options
3. If we complete all assignments, success
4. If any assignment fails, restart with fresh randomization
5. Repeat until success or `max_seconds` timeout

**Limitations:** No solution exists if the constraint graph makes a valid cycle impossible. The algorithm will timeout after `max_seconds` in such cases.