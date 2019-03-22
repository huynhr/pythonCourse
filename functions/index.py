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
# print(output)

# def test(item1, item2):
#     print(item1, item2)

# test(item1='cat', item2='dog')


def display_info(a, b, *args, instructor="Colt", **kwargs):
  return [a, b, args, instructor, kwargs]
#   print(type(args))


# print(display_info(1, 2, 3, instructor='ass', last_name="Steele", job="Instructor"))
# [1, 2, (3,), 'ass', {'last_name': 'Steele', 'job': 'Instructor'}]
