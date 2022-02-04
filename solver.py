from english_words import english_words_set
import random

WORD_LENGTH = 5
N_GUESSES = 6
N_WORDS = 1
ENGLISH_WORDS_LIST = [*english_words_set]
LIMIT = 6


class GridGenerator:
    def __init__(self, word_length = WORD_LENGTH, n_guesses = N_GUESSES) -> None:
        self.word_length = word_length
        self.n_guesses = n_guesses 
        self.empty_grid = self._generate_empty_grid()

    def _generate_empty_grid(self) -> list:
        row = []
        grid = []
        for _ in range(self.word_length):
            row.append('?')
        for _ in range(self.n_guesses):
            grid.append(row)
        return grid 

class AnswerGenerator:
    def __init__(self) -> None:
        self.eligible_words = [w.lower() for w in ENGLISH_WORDS_LIST if len(w) == WORD_LENGTH]
        self.word = self._select_word()

    def _select_word(self) -> list:
        return random.sample(self.eligible_words, N_WORDS)[0]

class WordGuesser:
    def __init__(self) -> None:
        self.eligible_words = [w.lower() for w in ENGLISH_WORDS_LIST if len(w) == WORD_LENGTH]
        self.remaining_words = self.eligible_words
        self.current_grid = GridGenerator().empty_grid
        self.word_guess = ['.']*WORD_LENGTH
        self.letters_in_diff_position = []
        self.letters_not_in_word = []
        self.guesses = 0
        self.current_row = 0
        self.current_word = None
        self.solved = False

    def guess_word(self):
        if self.guesses == 0:
            print(f"on guess {self.guesses} the word is about")
            return 'about'
        else:
            word = random.sample(self.remaining_words, 1)[0]
            print(f"on guess {self.guesses} the word is {word}")
            return word
       

    def insert_word_into_grid(self):
        self.current_word = self.guess_word()
        self.current_grid[self.current_row] = [c for c in self.current_word]
        self.update_row()
    
    def update_guesses(self):
        self.guesses += 1
    
    def update_row(self):
        self.current_row +=1
    
    def evaluate_word(self):
        for index, letter in enumerate(self.current_word):
            if answer[index] == letter:
                self.word_guess[index] == letter
            elif letter in answer:
                self.letters_in_diff_position.append(letter)
            elif letter not in answer:
                self.letters_not_in_word.append(letter)

    def reduce_potential_words(self, verbose = False):
        for index, letter in enumerate(self.word_guess):
            if letter == '.':
                pass 
            else:
                self.remaining_words = [word for word in self.remaining_words if word[index] == letter]
        
        for letter in self.letters_in_diff_position:
            self.remaining_words = [word for word in self.remaining_words if letter in word]

        for letter in self.letters_not_in_word:
            self.remaining_words = [word for word in self.remaining_words if letter not in word]
       
        if verbose:
            print(f"the number of remaining words is {len(self.remaining_words)}")

    def check_if_soved(self):
        if len(self.remaining_words) == 1 and self.remaining_words[0] == answer:
            self.solved = True
        else:
            pass

    def play_game(self):
        while self.guesses < LIMIT:
            self.insert_word_into_grid()
            self.evaluate_word()
            self.reduce_potential_words()
            self.update_guesses()
            self.check_if_soved()

            if self.solved:
                print(f"solved with word {self.remaining_words[0]} in {self.guesses} guesses")
                break
            else: 
                print(f"You have {len(self.remaining_words)} potential words remaining")
        
        if not self.solved:
             print(f"Problem failed. You had {len(self.remaining_words)} potential words remaining and exceeded the guess limit :(")

answers = AnswerGenerator()
answer = answers.word

w = WordGuesser()
w.play_game()


