from random import randint

random_num = randint(1, 10)
guess_num = int(input('Guess a number between 1 and 10: '))

while random_num != guess_num:
  if guess_num == random_num:
    print('You guessed it!')
  elif guess_num > random_num:
    print('To high!')
  elif guess_num < random_num:
    print('lower')
  play_again = input('Do you want to play again? (y/n) ')
  if play_again == 'n':
    break
  else:
    guess_num = int(input('Guess a number between 1 and 10: '))
