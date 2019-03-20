# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donations = 0
# for donation in donations.values():
#     total_donations += donation

# print(total_donations)

# output = {}.fromkeys(['email', 'fish', 'dog'], 'undefined')
# output.update({'planet': 'undefined'})
# output.update({'planet': 'Earth'})
# print(output.items())

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(len(list1))}
