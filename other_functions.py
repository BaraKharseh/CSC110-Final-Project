"""CSC110 Fall 2021 Project - Other Functions

File containing functions useful to main with no other home. Used by main to draw pygame objects
and convert strings of class attributes to the corresponding header string.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of CSC110 instructors at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Bara Kharseh and Patrick Fidler.
"""
import pygame


def checkbox_array(screen: all, x: int, y: int, boxes: int) -> None:
    """Draws a specified number of checkboxes at (x, y) in a column at a pre-determined size.

    Preconditions:
        - screen is a surface (pygame.display.
    """
    for _ in range(boxes):
        pygame.draw.rect(screen, 0, (x, y, 20, 20), 2)
        y += 35


def convert_name(name: str) -> str:
    """Used to convert strings of class attributes to their corresponding header strings."""
    if name == 'r_staff_hours':
        return 'Reduced staff hours or shifts'
    elif name == 'i_staff_hours':
        return 'Increased staff hours or shifts'
    elif name == 'r_salaries':
        return 'Reduced salaries or wages'
    elif name == 'froze_salaries':
        return 'Froze salaries or wages'
    elif name == 'i_salaries':
        return 'Increased salaries or wages'
    elif name == 'froze_bonus':
        return 'Froze bonus payments'
    elif name == 'delayed_compensation':
        return 'Delayed compensation'
    elif name == 'hired_staff':
        return 'Hired more staff'
    else:
        return 'Laid off staff'


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.check_all(config={
        'extra-imports': ['pygame'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
