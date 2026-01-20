import random
def passwordGenerator():
#define lists#
    lower_chars = ['a','b','c','d']

    upper_chars = ['A','B','C','D']

    special_chars = ['$','@','!','&','#','*']

    numeric_chars = [1,2,3,4,5,6,7,8,9,]

    password = random.choice(lower_chars) + random.choice(upper_chars) + random.choice(special_chars) + random.choice(numeric_chars)

    password = password + password 

    return password

print(passwordGenerator)
