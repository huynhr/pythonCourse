# times = input('How many times did I say to clean your room? ')
# times = int(times)

# for i in range(times):
#   print(i)

# animals = ['cat', 'dog']
# for idx, animal in enumerate(animals):
#   print(idx, animal)


# for x in range(1, 21):
#   if x == 4 or x == 13:
#     print(f'{x} is unlucky')
#   elif x % 2 == 0:
#     print(f'{x} is even')
#   else:
#     print(f'{x} is odd')

# print out smiley face pyramid from 1 - 10
# iterate through the number of rows 10 times
# each nested loop will print out he number of it's iterator
# for i in range(1, 11):
#   row = i
#   rowStr = ''
#   for j in range(i):
#     rowStr += '\U0001f600 '
#   print(rowStr)

# num = 1
# while num < 11:
#   print('*' * num)
#   num += 1

# spaces = 4
# for i in range(1, 11, 2):
#   smileyString = '*' * i
#   output = (spaces * ' ') + smileyString + (spaces * ' ')
#   spaces -= 1
#   print(output);

def printPryamid(height):
  height *= 2
  spaces = 0
  if height % 2 == 0:
    spaces = int(height / 2) - 1
  else:
    spaces = int(height/2)
  for i in range(1, height + 1, 2):
    smileyString = '*' * i
    output = (spaces * ' ') + smileyString + (spaces * ' ')
    spaces -= 1
    print(output)

printPryamid(9)