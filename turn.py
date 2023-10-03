import random

def play_human_turn(n):
  human_num = int(input("Your turn.Enter a number between 1 and 3 inclusive: "))
  if human_num >= 1 and human_num <= 3:
    n-= human_num
    print ("Current number is: " + str(n))
    if n<=0:
      print ("Congratulations, you win!")
      return 0
    else:
      play_computer_turn(n)
  else:
    print("Please enter a valid number between 1 and 3.")
    play_human_turn(n)


def play_computer_turn(n):
  if n % 4 == 0:
    computer_move = random.randint(1, 3)
  else:
    computer_move = n%4
  n -= computer_move

  if n == 0:
    print("Computer wins!!!")
    return 0
  return n


def countdown_game():
  print("Welcome to the countdown from 21 game!!!")
  starting_number = 21
  print("Starting number is: + starting_number)
  user_turn(starting_number)
