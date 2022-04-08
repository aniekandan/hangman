from game import Game


g = Game()

# ask if user wants to play again
user_input = "yes"

while user_input == "yes":
    # enter game play loop
    g.play()

    # ask if user wants to play again
    print("To play again, enter 'yes', but enter any other input to exit")
    user_input = input("Play again? ").lower()
