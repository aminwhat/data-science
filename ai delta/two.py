import numpy as np


def manage_cafe(n, requests):
    """
    Manages a cafe with n computers and handles m groups of customers.

    Args:
      n: Number of computers in the cafe.
      requests: A list of tuples (s, l), where s is the starting index and l is the length of the desired seating for each group.

    Returns:
      None
    """
    occupied = np.zeros(n, dtype=bool)
    for s, l in requests:
        # Find all potential starting indices with sufficient space
        potential_starts = np.arange(n - l + 1)

        # Check if any potential starting index leads to a valid seating arrangement
        valid_starts = potential_starts[
            np.all(occupied[potential_starts : potential_starts + l] == False)
        ]

        # Check if a valid seating arrangement exists
        if len(valid_starts) == 0:
            print("NO")
            continue

        # Choose the first valid starting index (flexible based on prioritization)
        first_valid_start = valid_starts[0]

        # Occupy the chosen segment
        occupied[first_valid_start : first_valid_start + l] = True

        # Print the final state of the cafe
        print("".join(["1" if x else "0" for x in occupied]))


# Example usage
n = 6
requests = [(2, 3), (1, 3), (1, 2), (3, 1), (1, 2)]

manage_cafe(n, requests)
