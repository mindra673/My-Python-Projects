import art
import random
import replit

def blackjack_game_start():
  
  print(art.logo)
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  computer_hand=[random.choice(cards), random.choice(cards)]
  print(f"Computer:  {computer_hand[0]}, 'X'")
  user_hand=[random.choice(cards), random.choice(cards)]
  print(f"User:  {user_hand[0]}, {user_hand[1]}")
  print(f"Computer Total:  {computer_hand[0]}")
  user_sum= user_hand[0]+user_hand[1]
  computer_sum= computer_hand[0]+computer_hand[1]
  print(f"User Total:  {user_sum}")
  
  if user_sum==21:
    print("User has Blackjack. User win!")
    return

  if computer_sum==21:
    print(f"Computer:  {computer_hand[0]}, {computer_hand[1]}")
    print("Computer has Blackjack. User lose!")
    return

  user_game_flag = True
  
  while user_game_flag == True:
    
    if user_sum>21:
      if 11 in user_hand:
        for i in range(user_hand[len(user_hand)-1]):
          if user_hand[i]==11:
            user_hand[i]=1
            break
        user_sum=user_sum-10
        if user_sum>21:
          print("User lose!")
          return
        else:
          print(f"Taking Ace value as 1.\nNew User Total:  {user_sum}")
          user_response= input("Do you want to Stand or Hit?\n")
          if user_response.lower()=="hit":
            user_hand.append(random.choice(cards))
            user_sum+=user_hand[len(user_hand)-1]
            print(f"New Card Drawn by User:  {user_hand[-1]}\nUser Total:  {user_sum}")
          else:
            user_game_flag= False
      else:
        print("User lose!")
        return

    else:
      user_response= input("Do you want to Stand or Hit?\n")
      if user_response.lower()=="hit":
        user_hand.append(random.choice(cards))
        user_sum+=user_hand[-1]
        print(f"New Card Drawn by User:  {user_hand[-1]}\nUser Total:  {user_sum}")
      else:
        user_game_flag= False

  print(f"Computer Total:  {computer_sum}")
  if computer_sum>21:
    if 11 in computer_hand:
      for i in range(computer_hand[len(computer_hand)-1]):
        if computer_hand[i]==11:
          computer_hand[i]=1
          computer_sum-=10
          break
    else:
      print("User win!")
      return
    
  while computer_sum<17:
    computer_hand.append(random.choice(cards))
    computer_sum+=computer_hand[-1]
    print(f"New Card Drawn by Computer:  {computer_hand[-1]}\nComputer Total:  {computer_sum}")
    if computer_sum>21:
      if 11 in computer_hand:
        for i in range(computer_hand[len(computer_hand)-1]):
          if computer_hand[i]==11:
            computer_hand[i]=1
            computer_sum-=10
            break
      else:
        print("User win!")
        return
    
  if user_sum>computer_sum:
    print("User Win!")
  elif user_sum==computer_sum:
    print("Draw")
  else:
    print("User lose!")

  return
    
  
match= True
while match:
  replit.clear()
  blackjack_game_start()
  rematch=input("Do you want to play again? Type yes or no.\n")
  if rematch=='no':
    match= False
