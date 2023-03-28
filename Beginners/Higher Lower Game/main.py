import art
import game_data
import random
import replit

print(art.logo)

def game():
    decider= True
    current_score=0
    
    while decider:
        prompt= random.sample(game_data.data,2)
        
        first_name=prompt[0]["name"]
        first_description=prompt[0]["description"]
        first_country=prompt[0]["country"]
        first_follower_count=prompt[0]["follower_count"]
        
        second_name=prompt[1]["name"]
        second_description=prompt[1]["description"]
        second_country=prompt[1]["country"]
        second_follower_count=prompt[1]["follower_count"]
        
        print(f"Compare A:  {first_name}, a {first_description}, from {first_country}.")
        print(art.vs)
        print(f"Against B:  {second_name}, a {second_description}, from {second_country}.")
        
        user_input=input("Who has more followers? Type 'A' or 'B': ")
        
        if user_input=='A':
            if first_follower_count>second_follower_count:
                replit.clear()
                print(art.logo)
                current_score+=1
                print(f"You're right! Current Score: {current_score}.")
            else:
                replit.clear()
                print(art.logo)
                print(f"Sorry, That's wrong. Final Score: {current_score}.")
                decider= False
        else:
            if second_follower_count>first_follower_count:
                replit.clear()
                print(art.logo)
                current_score+=1
                print(f"You're right! Current Score: {current_score}.")
            else:
                replit.clear()
                print(art.logo)
                print(f"Sorry, That's wrong. Final Score: {current_score}.")
                decider= False

game()
