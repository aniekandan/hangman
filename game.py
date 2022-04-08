from words import WordCache
import string

class Game:
    STAGE0 = [" ___ ", 
              "|   |", 
              "|   O",
              "|  /|\\", 
              "|   |", 
              "|  / \\", 
              "|    ", 
              "|    "]
    
    STAGE1 = [" ___ ", 
              "|   |", 
              "|   O",
              "|  /|\\", 
              "|   |", 
              "|  / ", 
              "|    ", 
              "|    "]
    
    STAGE2 = [" ___ ", 
              "|   |", 
              "|   O",
              "|  /|\\", 
              "|   |", 
              "|   ", 
              "|    ", 
              "|    "]
    
    STAGE3 = [" ___ ", 
              "|   |", 
              "|   O",
              "|  /| ", 
              "|   |", 
              "|    ", 
              "|    ", 
              "|    "]
    
    STAGE4 = [" ___ ", 
              "|   |", 
              "|   O",
              "|   | ", 
              "|   |", 
              "|    ", 
              "|    ", 
              "|    "]
    
    STAGE5 = [" ___ ", 
              "|   |", 
              "|   O",
              "|     ", 
              "|    ", 
              "|    ", 
              "|    ", 
              "|    "]
    
    STAGE6 = [" ___ ", 
              "|   |", 
              "|    ",
              "|     ", 
              "|    ", 
              "|    ", 
              "|    ", 
              "|    "]
    
    # the display stages of hangman. will be implemented
    # as a dictionary
    stages = None
    
    def __init__(self):
        self.__min_word_length = 5
        self.__max_word_length = 6
        
        # the maximum number of attempts, usually 6
        self.__max_attempts = 6
        
        # create the word cache to store the words later
        self.__cache = WordCache(self.__min_word_length, self.__max_word_length)
        
        # all letters of the alphabet in lowercase
        # helps restrict the possible inputs from user
        self.__alphabet = set(string.ascii_lowercase)
        
        # initiialize the display stages
        Game.stages = {
                6: Game.STAGE6, 5: Game.STAGE5, 4: Game.STAGE4,
                3: Game.STAGE3, 2: Game.STAGE2, 1: Game.STAGE1,
                0: Game.STAGE0
            }



    def __initial_state(self):
        return self.__cache.get_random_word(), self.__max_attempts
       
    
    
    def display_hangman(self, lives):
        return "\n".join(Game.stages[lives])
    
    
    
    def display_status(self, lives, guessed_letters, secret_word):
        # display the hangman
        print(self.display_hangman(lives))
        
        # inform user of the letters already used
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(guessed_letters))
        
        # display guess status, that is, the guessed word along
        # with underscores in place of unguessed words in the letter
        word_guess_status = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("Current progress: ", ' '.join(word_guess_status))
        

        
    def play(self):
        # main loop of game        
        secret_word, attempts = self.__initial_state()
        
        # stores letters available in the word
        # a way to keep track of letters that have been 
        # guessed in the current word. 
        letters_in_word = set(secret_word)
        
        # keep track of what user has guessed
        guessed_letters = set()        
        
        # display the status
        self.display_status(attempts, guessed_letters, secret_word)
        
        # repeat this loop while letters remaining in 
        # the word's character set is > 0 and lives left > 0
        while len(letters_in_word) > 0 and attempts > 0:        
            # get the user's input
            user_guess = input("Guess a letter: ").lower()
        
            # check if it is a valid letter not yet guessed
            unused_letters = self.__alphabet - guessed_letters
        
            if user_guess in unused_letters:       
                # user input has not yet been guessed
                # add the user's guess to the guessed letters set
                guessed_letters.add(user_guess)
                    
                # remove the letter from letters not yet guessed in secret word
                # if the guess is correct, Do this every 
                # time a correct guess is made. If a wrong guess
                # is made, reduce the lives by 1
                if user_guess in letters_in_word:
                    letters_in_word.remove(user_guess)
                        
                else:
                    attempts -= 1
                    
            elif user_guess in guessed_letters:
                # user made this guess before. 
                print("You have already guessed this letter! Try again.")
                    
            else:
                # user entered an invalid character
                print("You have entered an invalid character! Try again.")
                
                
            # display status
            self.display_status(attempts, guessed_letters, secret_word)

        # display the end message
        if attempts == 0:
            print("\nYou died! The word was '{}'".format(secret_word))
                
        else:
            print("\nYou won!!!")
