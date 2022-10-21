"""Some helpful utility functions for working with csv files."""

from csv import DictReader
from io import TextIOWrapper
from typing import Dict


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table/list of dictionaries."""
    result: list[dict[str, str]] = []
    # open the file
    file_handle: TextIOWrapper = open(filename, "r", encoding="utf8")

    # prepare to read the data file as a CSV rather than just strings
    csv_reader: DictReader[str] = DictReader(file_handle)

    # read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # close the file when done, to free its resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a simple column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columner(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result