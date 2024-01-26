import numpy as np


def identify(maxVal: int):
    if maxVal > 70:
        print("Win")
    else:
        print("Fail")


def make_array(arr):
    narr = np.array(arr)
    return narr


def random_number(user_input: int):
    rand_vals = np.random.randint(0, 101, size=user_input)
    return rand_vals
