from random import choice


# get ready to play some hangman
class Hangman(object):
    
    def __init__(self):
        # list of possible words
        self.word_list = open("words").readlines()
        self.playing = True
        
        while self.playing:
            self.won = False
            # boolean list keeping track of guessed letters
            self.already_guessed = []
            for i in range (0, 26):
                self.already_guessed.append(False)
            # 10 chances
            self.chances = 10
            # picks words and fixes blanks
            self.word = choice(self.word_list).upper()
            # the words have a space at the end for some reason so i'm fixing it with - 1
            self.letters_left = len(self.word) - 1
            self.print_word = []
            for i in range (0, len(self.word) - 1) :
                self.print_word.append("_")
            # keeps making guesses while chances left and player not done
            print("Welcome to Hangman! You have ten guesses.")
            while self.chances > 0 and not self.won:
                print("Your progress ::", "".join(self.print_word))
                self.make_guess()
            # if player won
            if self.won:
                print
                print("Congratulations! You correctly guessed %s" % (self.word))
            # if player lost
            else:
                print
                print("Sorry, you lost! The word was %s" % (self.word))
            # asks to play again
            play_again = input("Play again? Y for yes, N for no :: ").upper()
            while (not play_again == 'Y' and not play_again == 'N'):
                play_again = input("Sorry, didn't quite get that! Y for yes, N for no :: ").upper()
            if (play_again == 'N'):
                self.playing = False
                
    
    # makes a guess
    def make_guess(self):
        # is the guess acceptible
        good = False
        while (not good):
            print
            guess = input("Enter your guess :: ").upper()
            good = self.is_good(guess)
        self.check_guess(guess)
        
    # checks if guess is valid
    def is_good(self, guess):
        # in case of multiple letters
        if not len(guess) == 1:
            print("One letter at a time, try again!")
            return False
        # ascii val of guess
        val = ord(guess)
        # in case of non letter
        if val < 65 or val > 90:
            print("Guess must be a letter, try again!")
            return False
        # if letter already guessed
        if self.already_guessed[val - 65]:
            print("Already guessed, try again!")
            return False
        return True
      
    # checks if guess is correct
    def check_guess(self, guess):
        # marks letter as guessed
        self.already_guessed[ord(guess) - 65] = True
        # keeps track of how many times letter appears
        letter_count = 0
        for i in range (0, len(self.word)):
            if self.word[i] == guess:
                self.print_word[i] = guess
                letter_count += 1
        # letter not in word
        if letter_count == 0:
            self.chances -= 1
            print("Nope! %d chances remaining." % (self.chances))
        # letter in word
        else:
            # decreases number of letters left to guess
            self.letters_left -= letter_count
            print("%s appeared %d times!" % (guess, letter_count))
            # checks if player won
            if self.letters_left == 0:
                self.won = True
                
game = Hangman()