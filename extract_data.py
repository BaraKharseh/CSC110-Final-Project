"""CSC110 Fall 2021 Project - Extract Data

File used to extract data from initial_staffing_data.csv and change_staffing_data.csv. Places these
values into a list of StaffingData (a dataclass).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of CSC110 instructors at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Bara Kharseh and Patrick Fidler.
"""
import csv
from dataclasses import dataclass


@dataclass
class StaffingData:
    """A custom data type that represents the data taken from initial_staffing_data.csv
    or change_staffing_data.csv.

    Instance Attributes:
        - name: the name of the province/territory, or the industry or the size of the business
        - type: the type of staffing data
        - r_staff_hours: percent of businesses in name that reduced staff hours or shifts
        - i_staff_hours: percent of businesses in name that increased staff hours or shifts
        - r_salaries: percent of businesses in name that reduced salaries or wages
        - froze_salaries: percent of businesses in name that froze salaries or wages
        - i_salaries: percent of businesses in name that increased staff hours or shifts
        - froze_bonus: percent of businesses in name that froze bonus payments
        - delayed_compensation: percent of businesses in name that delayed compensation
        - hired_staff: percent of businesses in name that hired staff
        - laid_off_staff: percent of businesses in name that laid off staff

    Representation Invariants:
        - self.type in {'Province/Territory', 'Industry', 'Size'}
        - self.name is not ''
    """
    name: str
    type: str
    r_staff_hours: float
    i_staff_hours: float
    r_salaries: float
    froze_salaries: float
    i_salaries: float
    froze_bonus: float
    delayed_compensation: float
    hired_staff: float
    laid_off_staff: float


def read_csv_file(filename: str) -> list[StaffingData]:
    """Return the data stored in a csv file with the given filename.
    The return value is a list of StaffingData.

    Preconditions:
      - filename refers to a valid csv file
    """
    with open(filename) as file:
        reader = csv.reader(file)
        _ = next(reader)

        data = []
        count = 0

        for row in reader:
            data.append(process_row(row, count))
            count += 1

    return data


def process_row(row: list[str], count: int) -> StaffingData:
    """Convert a row of staffing data to a StaffingData object.

    Preconditions:
        - row has the correct format for staffing data set
    """
    return StaffingData(
        row[0],  # name
        find_type(count),  # type
        float(row[1]),  # r_staff_hours
        float(row[2]),  # i_staff_hours
        float(row[3]),  # r_salaries
        float(row[4]),  # froze_salaries
        float(row[5]),  # i_salaries
        float(row[6]),  # froze_bonus
        float(row[7]),  # delayed_compensation
        float(row[8]),  # hired_staff
        float(row[9]),  # laid_off_staff
    )


def find_type(count: int) -> str:  # helper function
    """Return the type for the instance attribute type in StaffingData."""
    if count in range(14):
        return 'Province/Territory'
    elif count in range(14, 30):
        return 'Industry'
    elif count in range(30, 34):
        return 'Size'
    else:
        return 'None'


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.check_all(config={
        'extra-imports': ['csv', 'dataclass'],
        'allowed-io': ['read_csv_file'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
