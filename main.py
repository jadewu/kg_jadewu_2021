import sys

# Read arguments
s1 = sys.argv[1]
s2 = sys.argv[2]

# The function for solving this question
def one_to_one(s1, s2):
    # Use set in python to remove duplicated elements
    l1 = list(set(s1))
    l2 = list(set(s2))
    # If there are more or equal unique elements in s1 than in s2, correct mapping
    if len(l1) >= len(l2):
        return True
    return False
print(one_to_one(s1,s2))

'''
# Debugging samples
print(one_to_one("abc", "bcd"))
print(one_to_one("foo", "bar"))
print(one_to_one("bar", "foo"))
print(one_to_one("aaaab", "ac"))
print(one_to_one("aabcaa", "abcd"))
print(one_to_one("", ""))
print(one_to_one("a", ""))
print(one_to_one("", "a"))
'''



