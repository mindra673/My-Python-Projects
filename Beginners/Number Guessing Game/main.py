import art
import random
import replit
def game():
  replit.clear()
  print(art.logo)
  print("Welcome to the Number Guessing Game!\nI am thinking of a Number between 1 and 100")
  number=random.randint(1,100)
  difficulty=input("Choose the difficulty level. Type easy or hard:  ")
  if difficulty.lower()=='easy':
    guess_count=10
  elif difficulty.lower()=='hard':
    guess_count=5
  result_flag=False
  while guess_count>0:
    print(f"You have {guess_count} attempts remaining to guess the number.")
    user_guess=int(input("Make a guess:  "))
    if user_guess>number:
      print("Too high.\nGuess again.")
    elif user_guess<number:
      print("Too low.\nGuess again.")
    else:
      result_flag=True
      print("You won, dude. Congratulations!")
      break
    guess_count-=1
  if not result_flag:
    print("You lost, dude. Shit happens :(")

match_flag=True

while match_flag:
  game()
  rematch=input("Do you want to play again? Type yes or no:  ")
  if rematch.lower()=='no':
    match_flag=False
    print("Good Bye! See you soon")
