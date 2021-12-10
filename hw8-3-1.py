# Author: SCT (AMDG) 12/9/21

def count_odds(lst):
    odd = 0
    x = 0

    while x < len(lst):
        if lst[x] % 2 != 0:
            odd += 1
        x += 1
    return odd

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)

