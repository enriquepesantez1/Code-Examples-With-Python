# This program runs a guessing game where the user has to find out what the animal is


# This is the main function that runs the game
def GuessingGame():
    # Declaring the local variables for the game
    numberOfUserTries = 1
    animal = "elephant"
    print("This program is thinking about an anmial. Can you geuss it?")
    guess = input("Enter your guess:").lower()
    #While loop that checks if the user is guessing right
    while animal != guess:
        if animal != guess and numberOfUserTries == 1:
            guess = input("Your guess was wrong. Try again: ").lower()
            numberOfUserTries = numberOfUserTries + 1 
            continue
        elif animal != guess and numberOfUserTries == 4:
            print(" Hiint: Its the biggest land animal in the world")
            guess = input("Try again: ").lower()
            numberOfUserTries = numberOfUserTries + 1
            continue
        else:
            break
    #Prints the awsner if the guess is right
    print("You got it! The animal was an elephant. The Number of Tries it took you: " + str(numberOfUserTries))


GuessingGame()