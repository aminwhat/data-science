list1 = list(input().split(" "))
list2 = list(input().split(" "))

count: int = 0

for k, v in zip(list1, list2):
    if k == str(1) and k == v:
        count = count + 1

print(count)
