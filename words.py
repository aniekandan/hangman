import random

class WordCache:
    # Represents a store of words
    def __init__(self, min_word_length, max_word_length):
        self.__words = []
        
        # load the words from file
        self.__load_file(min_word_length, max_word_length)
        
        
    def __load_file(self, min_word_length, max_word_length):
        WORD_LIST = 'wordlist.txt'
        OPEN_PAR = '('
        CLOSE_PAR = ')'
        HYPHEN = '-'
        
        with open(WORD_LIST, 'r') as f:
            for word in f:
                # remove all leading and trailing spaces
                # from the word
                word = word.strip().lower()
                
                # check word that either have parenthesis or hyphens
                # or, smaller than min_word_length
                if (OPEN_PAR in word) or (CLOSE_PAR in word) or (HYPHEN in word):
                    continue  # Skip words containing parentheses.
                    
                elif (len(word) < min_word_length) or (len(word) > max_word_length):
                    continue  # Skip the word because it is too short or too long.
                    
                else:
                    self.__words.append(word)
                    
                    
    def get_random_word(self):
        # Get a random word from the wordlist
        return random.choice(self.__words)
        
