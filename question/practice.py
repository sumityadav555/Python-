# Find the First Non-Repeating Character

def first_unique_char(ste):
    char_count = {}

    for char in ste:
        char_count[char] = char_count.get(char, 0) + 1

    for index, char in enumerate(ste):
        if char_count[char] == 1:
            return index

    return -1

print(first_unique_char("leetcode"))       # Output: 0 ('l')
print(first_unique_char("loveleetcode"))   # Output: 2 ('v')
print(first_unique_char("aabb")) 

