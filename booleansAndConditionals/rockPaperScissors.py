from random import *

num = randint(0, 2)
choice = ['rock', 'paper', 'scissors']

userChoice = input('Choose rock, paper or scissors? ');

computerChoice = choice[num]

if userChoice:
  if userChoice == computerChoice:
    print(f'It\'s a draw! \n user: {userChoice}, computerChoice: {userChoice}')
  if userChoice == 'rock' and computerChoice == 'paper':
    print(f'Computer wins! user: {userChoice}, computer: {computerChoice}')
  if userChoice == 'rock' and computerChoice == 'scissors':
    print(f'User wins! user: {userChoice}, computer: {computerChoice}')
  if userChoice == 'paper' and computerChoice == 'rock':
    print(f'User wins!, user: {userChoice}, computer: {computerChoice}')
  if userChoice == 'paper' and computerChoice == 'scissors':
    print(f'Computer wins! user: {userChoice}, computer: {computerChoice}')
  if userChoice == 'scissors' and computerChoice == 'rock':
    print(f'Computer wins!, user: {userChoice}, computer: {computerChoice}')
  if userChoice == 'scissors' and computerChoice == 'paper':
    print(f'User wins!, user: {userChoice}, computer: {computerChoice}')
else:
  print('please enter a valid choice')