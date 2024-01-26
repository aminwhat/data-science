import argparse
import os
import time
import numpy as np
from game import random_number, make_array, identify


class App:
    def __init__(self) -> None:
        self.user_in = self.get_user_input()
        self.t1 = time.time()

    def get_user_input(self) -> int:
        user_in: int = -1
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument("user_inut")
            user_in = int(parser.parse_args().user_inut)
        except:
            print("Input is Not Valid")
            os._exit(0)

        return user_in

    def generate_random_number(self, user_in: int):
        return random_number(user_in)

    def make_array(self, arr):
        return make_array(arr)

    def get_max_val(self, array: np.ndarray) -> int:
        return array.max()

    def identify(self, maxVal: int):
        identify(maxVal)
        self.t2 = time.time()
        print("Time To Execute: " + str(self.t2 - self.t1))


app = App()
rand_vals = app.generate_random_number(app.user_in)
narr = app.make_array(rand_vals)
max_val = app.get_max_val(narr)
app.identify(max_val)
