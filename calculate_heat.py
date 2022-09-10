"""CSC110 Fall 2021 Project - Calculate Heat

File used to calculate a heat value. For our purposes, a heat value is a numerical representation
of the change between one percentage in initial_staffing_data.csv to its pair value in
change_staffing_data.csv.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of CSC110 instructors at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Bara Kharseh and Patrick Fidler.
"""


def heat_calculator(initial_percent: float, final_percent: float, sign: str) -> float:
    """Calculates the heat value (positive or negative) based on the increase/decrease from
    the initial value to the final value, and whether the percentages are from a negative
    atrribute or a positive one (a negative attribute being one that is "bad" if its percentage
    increased).

    Preconditions:
        - 0.1 <= initial_percent <= 100.0
        - 0.1 <= final_percent <= 100.0
        - sign in {'positive', 'negative'}

    >>> heat_calculator(2.0, 4.0, 'positive')
    2.0
    """
    relative_value = 0

    if final_percent > initial_percent:
        relative_value = final_percent / initial_percent

    if final_percent < initial_percent:
        relative_value = -initial_percent / final_percent

    if sign == 'negative':
        return -relative_value
    else:
        return relative_value


def evaluate_sign(attribute: str) -> str:
    """Evaluates the sign of a certain attribute in the StaffingData class.

    Preconditions:
        - attribute in {"r_staff_hours", "i_staff_hours", "r_salaries", "froze_salaries",
        "i_salaries", "froze_bonus", "delayed_compensation", "hired_staff", "laid_off_staff"}

    >>> evaluate_sign('i_staff_hours')
    'positive'
    """
    if attribute in {'i_staff_hours', 'i_salaries', 'hired_staff'}:
        return 'positive'
    else:
        return 'negative'


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.check_all(config={
        'extra-imports': [],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
