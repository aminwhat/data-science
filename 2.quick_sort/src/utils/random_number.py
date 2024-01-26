import numpy as np


def random_number(user_input: int):
    rand_vals = np.random.randint(0, 101, size=user_input)
    return rand_vals
