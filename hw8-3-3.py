# Author: SCT (AMDG) 12/9/21

def three_letter_words(lst):

    letters = 0
    x = 0

    while x < len(lst):
        if len(lst[x]) == 3:
            letters += 1
        x += 1
    return letters

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
