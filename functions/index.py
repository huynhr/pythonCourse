'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


# def is_palindrome(string):
#     return string == ''.join(string.strip()[::-1])

# print(is_palindrome('tacocat'))

def intersection(collection1, collection2):
    return list(set(collection1) & set(collection2))
    
output = intersection([1,2,3], [2, 3, 4]) #[2,3]
print(output)
