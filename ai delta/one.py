n = int(input())


delta_line_length = 2 * n - 1

current_line = 1
dots_between = -1

while current_line <= n:
    arr = []
    if current_line == 1:
        i = 0
        while i <= n * 2 - 2:
            arr.append(".")
            i = len(arr)
        arr.pop(n - 1)
        arr.insert(n - 1, "D")
    elif current_line == n:
        while len(arr) <= delta_line_length - 1:
            arr.append("D")
            if len(arr) <= delta_line_length - 1:
                arr.append(".")
    else:
        dots_between = dots_between + 2
        arr.append("D")
        i = 1
        while i <= dots_between:
            arr.append(".")
            i = len(arr)
        arr.append("D")
        while len(arr) <= n + (n - 2):
            arr.insert(0, ".")
            arr.append(".")

    print("".join(arr))
    current_line = current_line + 1
