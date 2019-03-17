numbers = list(range(1, 11))
# print(numbers)

# doubledNumbers = [num * 2 for num in numbers]
# print(doubledNumbers)

# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# odds = [num for num in numbers if num % 2 != 0]
# print(odds)

# write list comprehension if the number is even then multiply be 2 other wise divide by 2
# conditionalNumbers = [num*2 if num % 2 == 0 else num/2 for num in numbers]
# print(conditionalNumbers)

# answer = [name[0] for name in ["Elie", "Tim", "Matt"]]
# answer = [num for num in list(range(1, 5)) if num in list(range(3, 7))]
answer = [[i for i in range(0, 10)] for row in range(0, 10)]
print(answer)

answer2 = [name.lower() for name in ["Elie", "Tim", "Matt"][::-1]]
print(answer2)
