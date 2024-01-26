import time
import numpy as np


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    arr = np.array(arr)
    p = arr[len(arr) // 2]
    l = [x for x in arr if x < p]
    m = [x for x in arr if x == p]
    r = [x for x in arr if x > p]
    # l = arr[arr < p]
    # m = arr[arr == p]
    # r = arr[arr > p]

    print("p: " + str(p) + "\tl: " + str(l) + "\tm: " + str(m) + "\tr: " + str(r))
    return quicksort(l) + m + quicksort(r)


t1 = time.time()
h = [1, 2, 3, 4, 5, 6, 7, 23432, 12]
print(quicksort(h))

t2 = time.time()

print(t2 - t1)
