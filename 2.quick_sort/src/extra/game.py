import numpy as np


def identify(maxVal: int):
    """
    Determine where the max value is under condition to lose or win
    """

    if maxVal > 70:
        print("Win")
    else:
        print("Fail")


def make_array(arr):
    """
    Make a numpy array from a simple array
    """
    narr = np.array(arr)
    return narr


def random_number(user_input: int):
    """
    Generate a Random numpy array based on the size from the user_input
    """
    rand_vals = np.random.randint(0, 101, size=user_input)
    return rand_vals
