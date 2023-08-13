"""
Is Unique: Implement an algorithm to determine if a string has all unique 
characters. What if you cannot use additional data structures
"""

# Method 1: Using sets
def isUniqueUsingSets(given_str):
    str_set = set()
    for char in given_str:
        str_set.add(char)
    return len(given_str) == len(str_set)

# Time complexity : O(n) for traversing on the string
# Space Complexity : O(26) = O(1) because the max character is going to 26 or 256



# Method 2: Using an array and ascii code to fill up the places in the array
def isUniqueUsingArray(given_str):
    pass

# Time Complexity : O(n) for 


# Method 3: Without using any data structures (sort the string then use two 
#           pointers to check the adjacent positions)
def isUniqueWithoutDataStructure(given_str):
    pass






