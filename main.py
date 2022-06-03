import random


def numb_guess_human():
  random_number = random.randint(1,10)
  user_guess = 0
  count = 0
  while user_guess != random_number:
    print(random_number)
    count += 1
    user_guess = int(input('Guess a number from 1 to 10: '))
    print('Unlucky! Try again :/')
    
  print('Congrats you just guess the correct number with a 1 in 10 chance, it only took you ' + str(count) + ' tries!')
  

def numb_guess_computer():
  user_numb = int(input('Choose a number from 1 to 1000 for the computer to guess?: '))
  comp_guess = 0
  count = 0
  while comp_guess != user_numb:
    count += 1
    comp_guess = int(random.randint(0, 1001))
  print('The wizz kid computer guessed ' + str(user_numb) + ' correctly, It only took ' + str(count) + ' tries!')
