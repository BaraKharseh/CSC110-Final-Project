"""CSC110 Fall 2021 Project - Other Functions

File containing functions used to create double bar graph variables.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of CSC110 instructors at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Bara Kharseh and Patrick Fidler.
"""
import extract_data


def double_bar_graph_variables(
        business_type: str,
        staffing_decision: str,
        data_set1: list[extract_data.StaffingData],
        data_set2: list[extract_data.StaffingData]) -> tuple[list[str], list[float], list[float],
                                                             str, str]:
    """Returns the necessary variables to make a specific double bar graph, based on the type of
    business and staffing decision.

    These variables are the list of x-axis values, the list of the first y-axis values, the list
    of the second y-axis values, and the names of bar 1 and bar 2.

    Preconditions:
        - business_type in {'Province/Territory', 'Industry', 'Size'}
        - staffing_decision in {
                            'r_staff_hours',
                            'i_staff_hours',
                            'r_salaries',
                            'froze_salaries',
                            'i_salaries',
                            'froze_bonus',
                            'delayed_compensation',
                            'hired_staff',
                            'laid_off_staff'}
    """
    x = []
    y1 = []
    y2 = []

    for staff_data in data_set1:
        if staff_data.type == business_type:
            x.append(staff_data.name)
            y1_value = str_to_data(staff_data, staffing_decision)
            y1.append(y1_value)

    for staff_data in data_set2:
        if staff_data.type == business_type:
            y2_value = str_to_data(staff_data, staffing_decision)
            y2.append(y2_value)

    n1, n2 = str_to_names(staffing_decision)

    return (x, y1, y2, n1, n2)


def str_to_data(staffing_data: extract_data.StaffingData, staffing_decision: str) -> float:
    """Returns the correct float from staffing_data based on the staffing decision being graphed."""
    if staffing_decision == 'r_staff_hours':
        return staffing_data.r_staff_hours
    elif staffing_decision == 'i_staff_hours':
        return staffing_data.i_staff_hours
    elif staffing_decision == 'r_salaries':
        return staffing_data.r_salaries
    elif staffing_decision == 'froze_salaries':
        return staffing_data.froze_salaries
    elif staffing_decision == 'i_salaries':
        return staffing_data.i_salaries
    elif staffing_decision == 'froze_bonus':
        return staffing_data.froze_bonus
    elif staffing_decision == 'delayed_compensation':
        return staffing_data.delayed_compensation
    elif staffing_decision == 'hired_staff':
        return staffing_data.hired_staff
    else:
        return staffing_data.laid_off_staff


def str_to_names(staffing_decision: str) -> tuple[str, str]:
    """Returns the correct bar names based on the staffing decision being graphed."""
    if staffing_decision == 'r_staff_hours':
        return ('Reduced Staff Hours (April 29th)', 'Reduced Staff Hours (July 14th)')
    elif staffing_decision == 'i_staff_hours':
        return ('Increased Staff Hours (April 29th)', 'Increased Staff Hours (July 14th)')
    elif staffing_decision == 'r_salaries':
        return ('Reduced Salaries (April 29th)', 'Reduced Salaries (July 14th)')
    elif staffing_decision == 'froze_salaries':
        return ('Froze Salaries (April 29th)', 'Froze Salaries (July 14th)')
    elif staffing_decision == 'i_salaries':
        return ('Increased Salaries (April 29th)', 'Increased Salaries (July 14th)')
    elif staffing_decision == 'froze_bonus':
        return ('Froze Bonuses (April 29th)', 'Froze Bonuses (July 14th)')
    elif staffing_decision == 'delayed_compensation':
        return ('Delayed Compensation (April 29th)', 'Delayed Compensation (July 14th)')
    elif staffing_decision == 'hired_staff':
        return ('Hired Staff (April 29th)', 'Hired Staff (July 14th)')
    else:
        return ('Laid off Staff (April 29th)', 'Laid off Staff (July 14th)')


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.check_all(config={
        'extra-imports': ['extract_data'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
