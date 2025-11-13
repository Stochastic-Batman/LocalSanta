# LocalSanta

Secret Santa, but only give gifts to people you actually know.

# Inputs

3 types of inputs are accepted with formats (values can have starting/trailing spaces; they will be stripped):

1. `.csv`. Example:

In Markdown a table needs a header separator row. Use this:

| lado | aneli | tsula |
|------|-------|-------|
| nita | ana   | luka  |

Or as a fenced code block (if you want to show the raw Markdown):

| lado | aneli | tsula |
|------|-------|-------|
| nita | ana   | luka  |

2. `.xlsx`. An Excel file where the first cell of each row is a person and the remaining cells in that row are people they might gift.

3. `.json`. A JSON file where each key is a person and the value is a list of people they might want to give a gift.

# Setup

You only have to run this `pip install` in case you have your data provided in `.xlsx` (Excel) format:

`pip install openpyxl`