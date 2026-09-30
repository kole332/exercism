"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate preparation time.
    
    :param number_of_layers: int - number of layers for lasagna.
    :return: int - preparation time of the lasagna (in minutes).

    Function that takes number of layers of lasagna as an argument and returns
    how many time the lasagna needs for preparation based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate total elapsed time.
    :param number_of_layers: int - number of layers of lasagna.
    :param elapsed_bake_time: int - time taken for baking the lasagna (in minutes).
    :return: int - total time needed for preparation and baking of the lasagna.

    Function that takes number of layers and elapsed bake time as arguments and
    calculate the total time needed for preparation and baking of the lasagna based
    on `PREPARATION_TIME` and `EXPECTED_BAKE_TIME`
    """
    return PREPARATION_TIME * number_of_layers + elapsed_bake_time


