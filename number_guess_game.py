import random

random_number = random.randint(1,100)
#print(random_number)

# Welcome message and instructions

print("Welcome to CAN YOU GUESS IT?")
print("Hi! I am Carl and I will be your opponent for today!")
print("The game is simple.\n I'm thinking of a number between 1 and 100.")

print("Go ahead and choose a difficulty level: \n *chances vary depending on level*")
print("1. Easy (10 chances) \n2. Medium (5 chances) \n3.Hard (3 chances)")

print("Enter your choice: ")

# Choice, chances and message depending on difficulty 
difficulty_choice = int(input())

difficulty_map = {1:10, 2:5, 3:3}
chances = difficulty_map.get(difficulty_choice)

difficulty_message = {1: "Easy Peasy Lemon Squeezy \nYou have selected the Easy difficulty level! Let's go! ",
                      2: "Not too hot, not too cold but just in the middle!\nYou have selected the Medium difficulty level. Let's go!", 
                      3: "Woahh, guess you like a challenge then. \nYou have selected the Hard difficulty level. Lets go!"}

# Game logic 
def play_game(chances):
    # Loop: iterations depend on difficulty choice 
    for x in range(chances): 
        print("Enter your guess: ")
        user_guess = int(input())
        
        if(user_guess == random_number):
            print(f"Congratulations! You guessed the correct number in {x+1} attempts.")
            print("Guess that makes you the winner, and me a loser :(")
            break
        
        elif (user_guess > random_number): 
            print("Hmmm...your number is bigger than mine. Ha! Try again.")
    
        elif (user_guess < random_number):
            print("Ahhhh, now you are smaller than my number, give it another go.")
        else: 
            print("Incorrect! Haha, why dont you try again")
    else: 
        print(f"Aww, bummer looks like you ran out of chances. Better luck next time buddy.\n The number i was thinking was: {random_number}")

# Game functionality 
# play_again variable allows user to choose if they wish to play again

play_again = "Y"
while play_again != "N":
    if chances:
        print(difficulty_message.get(difficulty_choice))
        play_game(chances)    
    else: 
        print("You did not choose a correct difficulty level.")      
    
    print("Wanna play again? (Y/N): ")
    play_again = str(input()).strip().upper()
      
        

