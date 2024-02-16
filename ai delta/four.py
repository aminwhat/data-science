def find_plaque(x, y):
    """
    Calculates the plaque number for a given house in the infinite city,
    handling edge cases and providing explanations.

    Args:
      x: X-coordinate of the house.
      y: Y-coordinate of the house.

    Returns:
      The plaque number of the house, or -1 if the house is not located
      on a valid intersection.
    """

    # Handle non-positive coordinates gracefully
    if x <= 0 or y <= 0:
        return -1  # Indicate invalid house location

    # Convert negative coordinates to positive for consistent calculations
    x = abs(x)
    y = abs(y)

    # Calculate distance from x-axis (adjusted for edge cases)
    distance_from_x_axis = max(y - 1, 0)  # Ensure non-negative distance

    # Calculate plaque number using absolute values
    plaque = x * distance_from_x_axis

    return plaque


# Get number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Get coordinates
    x, y = map(int, input().split())

    # Find and print plaque number
    plaque = find_plaque(x, y)
    if plaque == -1:
        print("Invalid house location")
    else:
        print(plaque)
